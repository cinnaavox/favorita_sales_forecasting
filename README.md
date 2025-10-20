# 🛒 Favorita – Grocery Sales Forecasting  
**Julia Felgentreu – Data Analyst**

---

## 🎯 Projektziel
Dieses Projekt untersucht die täglichen Verkaufszahlen der ecuadorianischen Supermarktkette **Corporación Favorita**,  
um Muster, Trends und externe Einflüsse (Feiertage, Ölpreise, Perishables) zu identifizieren  
und daraus **präzise Demand Forecasts** für die Region **Guayas (Jan–Mär 2014)** zu erstellen.

Das Projekt wurde im Rahmen des **Masterschool Time Series & Forecasting Tracks** umgesetzt  
und gipfelt in einem funktionsfähigen **Forecast-System (inkl. optionaler Streamlit-App)** für Demand Planner.

---

## 🔍 Projektstruktur & Workflow

| Ordner | Inhalt |
|--------|--------|
| **data/** | Eingangsdatensätze (Holidays, Oil Prices, Items, Stores, Transactions, Train) |
| **notebooks/** | Week 1–3 Notebooks (EDA, Feature Engineering, Modeling) |
| **app/** | (Optional) Streamlit-App zur Forecast-Visualisierung |
| **model/** | Utility-Funktionen (Load, Predict, Conformal Intervals) |
| **artifacts_week2_3/** | Forecast-Ergebnisse, Plots & Validierungsreports |
| **docs/** | Präsentationen, Zusammenfassungen, Reports |
| **requirements.txt** | Projektabhängigkeiten |

---

## 🧩 Ablauf

1️⃣ **Datenimport & Bereinigung**  
Nullwerte, negative Sales, Outlier-Capping, Kalenderaufbau  

2️⃣ **Feature Engineering**  
Lag-Features, Rolling Means, Datums-Komponenten, Oil & Holiday-Einflüsse  

3️⃣ **Exploratory Data Analysis**  
Trends, Seasonality, Autokorrelation, STL-Decomposition  

4️⃣ **Modellierung (Week 3)**  
Baseline- und Tuned-XGBoost (reg:squarederror), LSTM als Vergleich  

5️⃣ **Forecast-Generierung (Week 4)**  
Vorhersagen für März 2014, Export als Forecast-CSV + Validierungsplots  

---

## 🧠 Insights (Kurzüberblick)

| Thema | Erkenntnis |
|-------|-------------|
| **Trend & Seasonality** | Verkaufszahlen steigen 2013–2017, Dezember = Peak |
| **Holiday Effect** | Feiertage verändern Nachfrage spürbar (Weihnachten ↑ / August ↓) |
| **Perishables vs. Non-Perishables** | ~35 % Perishables → höheres Waste-Risiko → Forecast-Genauigkeit entscheidend |
| **Oil Prices** | Kaum Korrelation (ρ ≈ –0.64) → Feature wenig relevant |
| **Autocorrelation** | Hohe Autokorrelation auf Lag 1, 7 & 30 → Lag-Features essenziell |
| **Stationarität** | Nicht stationär → Modelle mit Trend-/Saisonkomponenten bevorzugt (XGBoost > ARIMA) |

---

## 📈 Forecast-Ergebnisse – Guayas Q1/2014

**Ziel:** März 2014 täglich vorhersagen (Train bis Februar, Val = letzte 7 Tage Februar)

| Modell | MAE | RMSE | Bias | sMAPE |
|:--|--:|--:|--:|--:|
| XGB Baseline | **3.39** | **7.93** | –0.12 | 51.95 |
| XGB Tuned | 3.42 | 7.90 | –0.10 | 53.06 |
| LSTM (optional) | 6.98 | 13.49 | +0.85 | 87.14 |

**Tages-Summen (März):**  
Klares Trend-Fit, moderate Abweichungen an Promo-/Peak-Tagen.

![Daily Sum March](artifacts_week2_3/daily_sum_march_readme.png)

**Top Features (XGB):**
`roll_mean_7`, `lag_1`, `lag_7`, `transactions`, `day_of_week`, `onpromotion`

**Stabilität (Drift-Check):**  
PSI zeigt erwartete Verschiebungen bei **Oil** (global trendig) und **Transactions** (lokale Volatilität).  
→ siehe [`artifacts_week2_3/psi_latest.csv`](artifacts_week2_3/psi_latest.csv)

---

## 💻 Streamlit-App (optional)
**Zielgruppe:** Demand Planner in der Region Guayas  
**Zeitraum:** Jan–Mär 2014

**Funktionen:**
- Upload von CSV/Parquet mit Forecasts  
- Filter nach Store & Item  
- Plot: Forecast + optional 90 %-Konfidenzintervall  
- CSV-Download der gefilterten Vorhersagen  
- Multi-Day Forecasts innerhalb des gewählten Fensters

**Start (lokal):**
```bash
git clone https://github.com/cinnaavox/favorita_sales_forecasting.git
cd favorita_sales_forecasting
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app/main.py

🧮 Modell & Performance

Bestes Modell: XGBoost (reg:squarederror)
Val-RMSE: 7.93
Top-Features: roll_mean_7, lag_1, lag_14, transactions, dcoilwtico

🧭 Empfehlungen

Kalender- & Promo-Features stärker gewichten

Perishables täglich monitoren → Fresh-Delivery-Strategien

XGBoost statt ARIMA nutzen → robust gegen nicht-stationäre Signale

Forecast-App für N-Day Exploration und Feiertags-Impact ausbauen

📂 Datenquellen & Links

Dataset: Kaggle – Corporación Favorita Grocery Sales Forecasting

Colab-Notebooks: Week 1–3 (Analysis & Modeling)

Docs:

Week 2 Summary

Week 3 Summary

Präsentation: (Slides-Link hier einfügen)


---

## 🧩 5) „How to reproduce“ (also was Reviewer machen)

👉 **Wo:** unter dein README (direkt nach „Datenquellen & Links“) oder als eigenen Abschnitt  
👉 **Warum:** Reviewer können mit 3 Klicks dein Forecast reproduzieren  

```markdown
## ▶️ Reproduzieren (Colab oder lokal)

1. Öffne das Notebook `notebooks/week2_3.ipynb`  
2. Stelle sicher, dass `xgb_booster.json` und `features.json` im Ordner `artifacts_week2_3/` liegen  
3. Führe den Forecast-Block am Ende aus:
   ```python
   # erstellt /artifacts_week2_3/daily_sum_march_readme.png
   # und forecast_guayas_2014_03.csv

