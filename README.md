# 🛒 Favorita – Grocery Sales Forecasting  
**Julia Felgentreu – Data Analyst**

---

## 🎯 Projektziel  
Dieses Projekt untersucht die täglichen Verkaufszahlen der ecuadorianischen Supermarktkette **Corporación Favorita**,  
um Muster, Trends und externe Einflüsse wie **Feiertage, Ölpreise und Perishables** zu identifizieren  
und daraus präzise **Demand Forecasts für die Region Guayas (Jan–Mär 2014)** zu erstellen.

Das Projekt wurde im Rahmen des **Masterschool Time Series & Forecasting Tracks** umgesetzt  
und gipfelt in einem **funktionsfähigen Forecast-System**, das als Grundlage für eine interaktive App dienen kann.

---

## 🔍 Projektstruktur & Workflow

| Ordner / Datei           | Inhalt                                                                 |
|---------------------------|------------------------------------------------------------------------|
| `data/`                  | Eingangsdatensätze (Holidays, Oil Prices, Items, Stores, Transactions, Train) |
| `notebooks/`             | Week 1–3 Notebooks (EDA, Feature Engineering, Modeling)                |
| `model/`                 | Utility-Funktionen (Load, Predict, Conformal Intervals)                |
| `artifacts_week2_3/`     | Forecast-CSV, Plots & Validierungsreports                              |
| `docs/`                  | Präsentationen, Zusammenfassungen, Reports                             |
| `requirements.txt`       | Projektabhängigkeiten                                                  |

---

## 🧩 Ablauf

1️⃣ **Datenimport & Bereinigung**  
   - Behandlung fehlender Werte, negativer Sales und Ausreißer  
   - Aufbau eines vollständigen Kalenders über alle Stores & Items  

2️⃣ **Feature Engineering**  
   - Lag-Features (1, 7, 14, 30 Tage)  
   - Rolling Means, Datums- und Zyklus-Komponenten  
   - Ölpreise, Feiertage & Promotion-Effekte  

3️⃣ **Exploratory Data Analysis (Week 1)**  
   - Trend, Saisonalität, Autokorrelation, STL-Decomposition  

4️⃣ **Modellierung (Week 3)**  
   - Baseline- und Tuned-XGBoost (reg:squarederror)  
   - Vergleich mit einfacher LSTM-Architektur  

5️⃣ **Forecast-Generierung (Week 4)**  
   - Vorhersagen für März 2014  
   - Export als Forecast-CSV und Validierungsplots  

---

## 🧠 Insights (Kurzüberblick)

| Thema                        | Erkenntnis                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| **Trend & Seasonality**      | Verkaufszahlen steigen 2013–2017, Dezember = Peak                         |
| **Holiday Effect**           | Feiertage verändern Nachfrage deutlich (Weihnachten ↑ / August ↓)          |
| **Perishables vs Non-Perish.** | ~35 % Perishables → höheres Waste-Risiko → Forecast-Genauigkeit entscheidend |
| **Oil Prices**               | Kaum Korrelation (ρ ≈ –0.64) → Feature wenig relevant                      |
| **Autocorrelation**          | Starke Autokorrelation bei Lag 1, 7 & 30 → Lag-Features essenziell         |
| **Stationarität**            | Nicht stationär → Modelle mit Trend/Saison bevorzugt (XGBoost > ARIMA)     |

---

## 📈 Forecast-Ergebnisse – Guayas Q1 / 2014  
Ziel: März 2014 täglich vorhersagen (Train bis Februar, Val = letzte 7 Tage Februar)

| Modell           | MAE  | RMSE | Bias   | sMAPE |
|------------------|------|------|--------|--------|
| XGB Baseline     | 3.39 | 7.93 | –0.12  | 51.95  |
| XGB Tuned        | 3.42 | 7.90 | –0.10  | 53.06  |
| LSTM (optional)  | 6.98 | 13.49| +0.85  | 87.14  |

**Tages-Summen (März):**  
Klares Trend-Fit, moderate Abweichungen an Promo- und Peak-Tagen.  

<img width="1186" height="468" alt="Vorhersage März 2014" src="https://github.com/user-attachments/assets/0382e900-19e5-495b-853c-1b0bf9e5b378" />

**Top Features (XGB):** `roll_mean_7`, `lag_1`, `lag_7`, `transactions`, `day_of_week`, `onpromotion`

**Stabilität (Drift-Check):**  
PSI zeigt erwartete Verschiebungen bei **Oil** (globaler Trend) und **Transactions** (lokale Volatilität).  
→ siehe **[PSI-Tabelle (CSV)](https://drive.google.com/file/d/1S5g9Yc8GWgKz5lxnDvBWzFanJI9lM6f3/view?usp=sharing)**  

**Vorhersage-CSV (März 2014, Guayas, XGB):**  
→ [Forecast CSV auf Google Drive ansehen](https://drive.google.com/file/d/1JZ7hEAYmTQ0mSELB7Kh7FvLgrbh5C7cu/view?usp=sharing)

---

🧮 Modell & Performance

Bestes Modell: XGBoost (reg:squarederror)

Val-RMSE: 7.93

Top-Features: roll_mean_7, lag_1, lag_14, transactions, dcoilwtico

🧭 Empfehlungen

Kalender- & Promo-Features stärker gewichten

Perishables täglich monitoren → Fresh-Delivery-Strategien

XGBoost statt ARIMA → robust gegen Nicht-Stationarität

Forecast-Tool zur operativen Planung weiterentwickeln (N-Day / Feiertags-Impact)

📂 Datenquellen & Links

Dataset: Kaggle – Corporación Favorita Grocery Sales Forecasting (https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)

Colab-Notebooks: Week 1 (https://colab.research.google.com/drive/1pwL5XJ3m_K0IMnNC5rhJpQnDRd9hA1P7?usp=drive_link) & Week 2/3 (https://colab.research.google.com/drive/1Cfv2uuvbo5gdbMaDB4E_RMCZcxlb2ZhX?usp=drive_link)

Docs: Week 1 Summary (https://docs.google.com/document/d/1KaC9j29FeOrFRx0SYh6ykhUiTYikI_yoyGlCh2kejdE/edit?usp=sharing), Week 2/3 Summary (https://docs.google.com/document/d/1e2etarC9O55nTqxsOjekTLad9WM2B5jkopWBHf2YIU0/edit?usp=drive_link)

Präsentation: (Slides-Link einfügen)

---

## 💻 Optionale Erweiterung: Streamlit-App  

Zur Demonstration der Ergebnisse kann das Projekt um eine interaktive **Streamlit-App** ergänzt werden.  
Diese dient als Forecast-Explorer für **Demand Planner in der Region Guayas** und erlaubt es, Vorhersagen für beliebige Stores und Artikel visuell zu untersuchen.

**Funktionen:**  
- Upload von CSV / Parquet mit Forecasts  
- Filter nach Store & Item  
- Plot mit 90 % Konfidenzintervall  
- CSV-Download der gefilterten Vorhersagen  
- Multi-Day-Forecasts innerhalb des gewählten Fensters  

**Lokaler Start (optional):**
```bash
git clone https://github.com/cinnaavox/favorita_sales_forecasting.git
cd favorita_sales_forecasting
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/main.py

Hinweis: Die App ist optional und diente als Experiment zur visuellen Exploration.
Das Kernziel des Projekts bleibt die Modellvalidierung & Prognosequalität.
