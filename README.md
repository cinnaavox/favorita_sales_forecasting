# 🛒 Favorita – Grocery Sales Forecasting  
*Julia Felgentreu – Data Analyst*

---

## 🎯 Projektziel

Dieses Projekt untersucht die täglichen Verkaufszahlen der ecuadorianischen Supermarktkette **Corporación Favorita**,  
um Muster, Trends und externe Einflüsse (Feiertage, Ölpreise, Perishables) zu identifizieren  
und daraus präzise **Demand Forecasts** zu erstellen.

Das Projekt wurde im Rahmen des **Time Series & Forecasting Tracks (Masterschool)** umgesetzt  
und gipfelt in einer interaktiven **Streamlit-App**, mit der Demand Planner Forecasts für  
Stores in der Region **Guayas** (Jan – Mär 2014) explorieren können.

---

## 🔍 Projektstruktur & Workflow

data/ – Eingangsdatensätze (Holidays, Oil Prices, Items, Stores, Transactions, Train-Sample)
notebooks/ – Analyse-Notebooks (Cleaning, EDA, Feature Engineering, Modeling)
app/ – Streamlit-App (UI & Config)
model/ – Model-Utility-Funktionen (Load, Predict, Conformal Intervals)
artifacts_local/ – Lokale ML-Artefakte (nicht im Git → .gitignore)
docs/ – Präsentation & Projektreports
images/ – Exportierte Plots & App-Screenshots
requirements.txt – Projektabhängigkeiten


---

## 🧩 Ablauf

1. **Datenimport & Bereinigung**  
   Nullwerte, negative Sales, Outlier-Capping, Kalenderaufbau  
2. **Feature Engineering**  
   Lag-Features, Rolling Means, Datumskomponenten, Ölpreise, Feiertage  
3. **Exploratory Data Analysis**  
   Trends, Seasonality, Autocorrelation, STL-Decomposition  
4. **Modellierung (Week 3)**  
   Baseline XGBoost mit Early Stopping, Mini-LSTM zum Vergleich  
5. **App-Entwicklung (Week 4)**  
   Streamlit-App zur Forecast-Visualisierung & Exploration  

---

## 🧠 Insights (Kurzüberblick)

| Thema | Erkenntnis |
|-------|-------------|
| **Trend & Seasonality** | Verkaufszahlen steigen 2013–2017, Dezember = Peak |
| **Holiday Effect** | Feiertage verändern Nachfrage spürbar (Weihnachten ↑ / August Dip) |
| **Perishables vs. Non-Perishables** | ~35 % Perishables → höheres Waste-Risiko → Forecast-Genauigkeit entscheidend |
| **Oil Prices** | Kaum Korrelation → Feature nicht essentiell |
| **Autocorrelation** | Hohe Autokorrelation auf Lag 1, 7 & 30 → Lag-Features wichtig |
| **Stationarität** | Nicht stationär → Modelle mit Trend/Saisonalität bevorzugen (XGBoost, LSTM) |

---

## 📈 Empfehlungen

- **Kalender- & Promotion-Features** stärker gewichten  
- **Perishable Items** täglich monitoren → Fresh-Delivery-Strategien  
- **XGBoost statt ARIMA** verwenden → robust gegen nicht-stationäre Signale  
- **Forecast App** als Tool für Planer nutzen → N-Day Exploration & Feiertags-Impact  

---

## 🧮 Modell & Performance

- **Bestes Modell:** XGBoost (reg:squarederror)  
- **Val-RMSE:** *(hier deine Zahl einfügen)*  
- **Top Features:** `roll_mean_7`, `lag_1`, `lag_14`, `transactions`, `dcoilwtico`

---

## 💻 Streamlit-App

**Zielgruppe:** Demand Planner in der Region Guayas  
**Zeitraum:** Jan – Mär 2014  

### 🚀 Quickstart (lokal)

```bash
# 1️⃣ Repo klonen
git clone https://github.com/cinnaavox/favorita_sales_forecasting.git
cd favorita_sales_forecasting

# 2️⃣ Umgebung einrichten
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# 3️⃣ Lokale Artefakte (aus Week 3) ablegen
mkdir -p artifacts_local
#   artifacts_local/xgb_booster.json
#   artifacts_local/features.json
#   artifacts_local/conformal_intervals.json (optional)

# 4️⃣ App starten
streamlit run app/main.py

---

📊 Funktionen

Upload: CSV/Parquet mit Features (Jan–Mär 2014)

Filter: Store + Item (SKU) Auswahl

Plot: Forecast + optional 90 % Konfidenzintervall

Download: CSV mit Vorhersagen

Multi-Day Forecast: automatisch für mehrere Tage innerhalb des gewählten Fensters

---

🧭 Anforderungen

app/
  main.py         – Streamlit UI
  config.py       – Pfade & Konstanten
data/
  data_utils.py   – Laden / Filtern
model/
  model_utils.py  – Laden / Predict / Conformal
requirements.txt  – Dependencies
.gitignore        – Ignoriert Artefakte & Caches

---

📂 Datenquellen & Links

Dataset: Kaggle – Corporación Favorita Grocery Sales Forecasting

Colab Notebooks: (Week 1–3 Analysis & Modeling)

Streamlit App: lokal ausführbar → Forecast Explorer Guayas Region

Präsentation: (Drive- oder Slides-Link einfügen)

