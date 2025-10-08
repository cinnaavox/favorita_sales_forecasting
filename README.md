# 🛒 Favorita – Grocery Sales Forecasting  
*Julia Felgentreu – Data Analyst*  

🎯 **Projektziel**  
Dieses Projekt untersucht die täglichen Verkaufszahlen der ecuadorianischen Supermarktkette *Corporación Favorita*,  
um Muster, Trends und externe Einflüsse (Feiertage, Ölpreise, Perishables) zu identifizieren.  
Ziel ist es, eine saubere, feature-reiche Zeitreihe zu erstellen, die als Grundlage für Forecasting-Modelle dient.  

---

🔍 **Projektstruktur & Workflow**  

- **data/** – Eingangsdatensätze (Holidays, Oil Prices, Items, Stores, Transactions, Train-Sample)  
- **notebooks/** – Analyse-Notebooks (Cleaning, EDA, Feature Engineering, Visualisierungen)  
- **scripts/** – Python-Hilfsskripte & Preprocessing-Module  
- **images/** – exportierte Plots und Grafiken für Dokumentation & Reports  
- **docs/** – Präsentation, Reports & Projektzusammenfassung  

**Ablauf**  
1. Datenimport & -bereinigung (Nullwerte, negative Sales, Outlier-Capping)  
2. Erstellung eines vollständigen Kalenders (kontinuierliche Zeitreihen pro Store-Item)  
3. Feature Engineering (Datumskomponenten, Rolling Averages, Perishable-Flag, Holidays, Ölpreise)  
4. Exploratory Data Analysis (Trends, Seasonality, Perishables vs. Non-Perishables, Holiday-Impact, Ölpreisvergleich)  
5. Advanced EDA (Autocorrelation, Stationarität, STL-Decomposition)  
6. Zwischenspeicherung des Cleaned Frames (Pickle)  

---

🧩 **Insights (Kurzüberblick)**  
- **Trend & Seasonality**: Verkaufszahlen steigen 2013–2017 kontinuierlich, klare Peaks im Dezember  
- **Holiday Effect**: Feiertage heben oder senken Nachfrage spürbar (z. B. Weihnachten = Spitzen, August 2017 = auffälliger Dip)  
- **Perishable vs. Non-Perishable**: ~35 % aller Verkäufe entfallen auf Perishables – hohes Risiko für Waste → Forecast-Genauigkeit entscheidend  
- **Oil Prices**: Kein klarer Zusammenhang zwischen Ölpreis und Nachfrage – wenig Mehrwert für Feature Engineering  
- **Autocorrelation**: Hohe Autokorrelation auf kurzen Lags (1, 7, 30 Tage) → Lag-Features sehr hilfreich  
- **Stationarität**: Daten sind nicht-stationär (starker Trend + Saisonalität)  

---

📊 **Wichtige Erkenntnisse**  
- Daten sind stark von Kalendereffekten (Wochenende, Feiertage, Saison) geprägt  
- Perishables benötigen präzisere Forecasts, da Fehlplanung schnell zu Verlusten führt  
- Ölpreis hat kaum Einfluss auf Nachfrage → Feature eher vernachlässigbar  
- Lag-Features & Rolling Averages sind zentrale Bausteine für spätere Modelle  

---

📈 **Empfehlungen**  
- Fokus auf Kalender- und Promotion-Features für Forecasting-Modelle  
- Perishable-Items eng überwachen → Daily Forecasts & Fresh-Delivery-Strategien  
- Non-stationäre Struktur beachten → differenzieren oder Modelle nutzen, die Trends/Saisonalität abbilden (XGBoost, LSTM)  
- Für klassische Modelle wie ARIMA → vorher Trend & Seasonality entfernen (STL, Differencing)  

---

📂 Quellen & Links  
- Kaggle Dataset: [Corporación Favorita Grocery Sales Forecasting](https://www.kaggle.com/c/favorita-grocery-sales-forecasting)  
- Colab-Notebooks: [Google Colab Link hier einfügen]  
- Report (EDA Summary): [Drive-Link oder PDF einfügen]  
- Präsentation: [Link einfügen, falls vorhanden] 
