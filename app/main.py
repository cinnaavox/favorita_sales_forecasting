import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional

from app.config import (
    ART_DIR, MODEL_PATH, FEATURES_PATH, CONFORMAL_PATH,
    DATE_MIN, DATE_MAX, TIME_COL, STORE_COL, ITEM_COL, MAX_SHOW_ROWS
)
from model.model_utils import load_artifacts, ensure_features, predict_xgb, apply_conformal
from data.data_utils import load_df, available_keys, filter_window, filter_series, thin_preview

st.set_page_config(page_title="Guayas Retail Forecast", layout="wide")
st.title("🛍️ Guayas Retail Forecast — Jan–Mar 2014")

with st.sidebar:
    st.header("1) Model-Artefakte")
    st.caption("Lege lokal in **artifacts_local/** ab (nicht im Git).")
    st.write(f"📁 `{ART_DIR}`")

    ok_model = Path(MODEL_PATH).exists()
    ok_feats = Path(FEATURES_PATH).exists()
    ok_conf  = Path(CONFORMAL_PATH).exists()

    st.write("Model:", "✅" if ok_model else "❌", MODEL_PATH.name)
    st.write("Features:", "✅" if ok_feats else "❌", FEATURES_PATH.name)
    st.write("Conformal (optional):", "✅" if ok_conf else "—")

    if not (ok_model and ok_feats):
        st.warning("Bitte `xgb_booster.json` und `features.json` in artifacts_local/ ablegen.")
    else:
        booster, FEATURES, TARGET, CONFORMAL = load_artifacts(MODEL_PATH, FEATURES_PATH, CONFORMAL_PATH)

    st.markdown("---")
    st.header("2) Daten laden")
    up = st.file_uploader("CSV/Parquet mit vorbereiteten Features (Jan–Mar 2014)", type=["csv","parquet"])
    sample_note = st.caption("Tipp: Nimm dein Q1-Feature-Export (Guayas, Top-3 Families).")

df: Optional[pd.DataFrame] = None
if up is not None:
    try:
      
        tmp_path = Path("data/cache") / up.name
        tmp_path.parent.mkdir(parents=True, exist_ok=True)
        with open(tmp_path, "wb") as f:
            f.write(up.getbuffer())
        df = load_df(tmp_path)
    except Exception as e:
        st.error(f"Konnte Datei nicht lesen: {e}")

if df is None:
    st.info("Bitte oben eine Datei laden. Danach kannst du Store/Item wählen.")
    st.stop()

stores, items = available_keys(df, STORE_COL, ITEM_COL)
colA, colB, colC = st.columns([1,1,2])
with colA:
    store = st.selectbox("Store", stores if stores else [None])
with colB:
    item = st.selectbox("Item (SKU)", items if items else [None])
with colC:
    st.write(" ")

if store is None or item is None:
    st.warning("Wähle Store & Item aus.")
    st.stop()

df_si = filter_series(df, int(store), int(item), STORE_COL, ITEM_COL)
if df_si.empty:
    st.error("Für diese Kombination gibt es keine Zeilen in der geladenen Datei.")
    st.stop()

col1, col2, col3 = st.columns([1,1,2])
with col1:
    start_date = st.date_input("Start", value=pd.to_datetime("2014-03-01"), min_value=pd.to_datetime(DATE_MIN), max_value=pd.to_datetime(DATE_MAX))
with col2:
    end_date = st.date_input("Ende", value=pd.to_datetime("2014-03-31"),  min_value=pd.to_datetime(DATE_MIN), max_value=pd.to_datetime(DATE_MAX))

start_date = pd.to_datetime(start_date)
end_date   = pd.to_datetime(end_date)
if start_date > end_date:
    st.error("Startdatum darf nicht nach Endedatum liegen.")
    st.stop()

df_win = filter_window(df_si, start_date, end_date, TIME_COL)
if df_win.empty:
    st.warning("Im gewählten Fenster gibt es keine Zeilen. Prüfe deine Datei/Features.")
    st.stop()

try:
    X = ensure_features(df_win, FEATURES)
    yhat = predict_xgb(booster, X)
    lo90, hi90 = apply_conformal(yhat, CONFORMAL)
    out = df_win[[TIME_COL, STORE_COL, ITEM_COL]].copy()
    out["pred"] = yhat
    if lo90 is not None and hi90 is not None:
        out["pred_lo90"] = lo90
        out["pred_hi90"] = hi90
except Exception as e:
    st.exception(e)
    st.stop()

st.subheader("Vorhersagen")
st.dataframe(out.head(MAX_SHOW_ROWS))

st.subheader("Plot (tägliche Vorhersagen)")
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,3))
plt.plot(out[TIME_COL], out["pred"], label="Forecast")
if "pred_lo90" in out and "pred_hi90" in out:
    plt.fill_between(out[TIME_COL], out["pred_lo90"], out["pred_hi90"], alpha=0.2, label="PI 90%")
plt.ylabel("Units")
plt.legend()
plt.tight_layout()
st.pyplot(fig)

st.download_button(
    "CSV herunterladen",
    out.to_csv(index=False),
    file_name=f"forecast_store{store}_item{item}_{start_date.date()}_{end_date.date()}.csv",
    mime="text/csv"
)

with st.expander("Hinweise"):
    st.markdown("""
- Diese App nutzt mein **XGBoost-Modell aus Week 3** – die Dateien liegen lokal in `artifacts_local/`.
- Multi-Day Forecasts funktionieren, **wenn im Upload-File alle Tages-Features bereits enthalten sind** (wie in meinem Q1-Export).
- Wähle oben Store & Item, lege den Zeitraum in **Jan–Mär 2014** fest, und sieh dir den Forecast inkl. optionalem 90%-Konfidenzintervall an.
- Für andere Zeiträume müssen die Features in den Notebooks neu berechnet werden (Lags, Rolling Means usw.).
""")
