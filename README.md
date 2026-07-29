# ✈️ AeroVision

> **Real-time Flight Analytics Dashboard powered by Python, OpenSky Network API, and Power BI**

AeroVision is an end-to-end data analytics project that collects live flight data from the OpenSky Network API, processes it through a Python ETL pipeline, and visualizes key aviation insights using an interactive Power BI dashboard.

The project demonstrates practical skills in API integration, data engineering, feature engineering, automation, and business intelligence by transforming raw aviation data into meaningful operational insights.

---

## 📌 Project Overview

Traditional dashboard projects often rely on static CSV datasets. AeroVision instead works with **live aviation data**, making every dashboard refresh display the latest flight information.

The project automatically:

- Fetches real-time flight data
- Cleans and validates raw records
- Performs feature engineering
- Generates analytics-ready datasets
- Updates an interactive Power BI dashboard

---

## 🚀 Features

- 🌍 Real-time flight tracking using OpenSky Network API
- 🔄 Automated ETL pipeline built in Python
- 🧹 Data cleaning and preprocessing
- 📊 Feature engineering for aviation analytics
- 📈 Interactive Power BI dashboard
- ⚡ Live dashboard refresh with updated flight information
- 📦 Modular Python project structure

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| API | OpenSky Network API |
| Visualization | Power BI |
| Authentication | OAuth 2.0 |
| Version Control | Git, GitHub |

---

## 🏗 Project Architecture

```text
                OpenSky Network API
                        │
                        ▼
                Authentication
                        │
                        ▼
               Fetch Live Flight Data
                        │
                        ▼
                 Data Cleaning
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
              Processed Dataset
                        │
                        ▼
                Power BI Dashboard
```

---

## 📂 Project Structure

```text
AeroVision/
│
├── assets/
├── docs/
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── auth.py
│   ├── fetch_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   └── eda.py
│
├── .env.example
├── .gitignore
├── main.py
├── powerbi_source.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/manish-jc/AeroVision.git
```

Navigate to the project

```bash
cd AeroVision
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

Run the project

```bash
python main.py
```

---

## 📊 Dashboard

Dashboard screenshots will be added here.

---

## 📈 Future Improvements

- Flight delay prediction
- Airport performance analytics
- Historical trend analysis
- Weather integration
- Airline performance comparison
- Real-time dashboard deployment using Power BI Service

---

## 👨‍💻 Author

**Manish J C**

- GitHub: https://github.com/manish-jc

---

## ⭐ If you found this project useful

Consider giving the repository a star!
