# 📊 TrendPulse – Real-Time Data Pipeline

TrendPulse is a Python-based data pipeline that fetches real-time trending news data using an API, processes and cleans it, performs exploratory data analysis (EDA), and visualizes insights.

---

## 🚀 Features

* Live API data collection
* Data cleaning & preprocessing
* Feature engineering
* Exploratory Data Analysis (EDA)
* Data visualization

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Requests

---

## 📂 Project Structure

* `task1_data_collection.py` → Fetches live data from API
* `task2_data_processing.py` → Cleans and preprocesses data
* `task3_analysis.py` → Performs EDA
* `task4_visualization.py` → Generates visual insights

---

## ▶️ How to Run

1. Add your API key in `task1_data_collection.py`
2. Run scripts in order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

---

## 📈 Outputs

### 🔹 Task 1 – Data Collection

* Output: `data/raw_data.csv`
* Contains real-time fetched news dataset

### 🔹 Task 2 – Data Processing

* Output: `data/cleaned_data.csv`
* Cleaned dataset with:

  * Removed duplicates
  * Handled missing values
  * Feature engineering (date, hour, lengths)

### 🔹 Task 3 – Analysis (EDA)

* Output: `task3_analysis.md`
* Includes:

  * Data overview
  * Source distribution
  * Time-based trends
  * Statistical summaries

---

### 🔹 Task 4 – Visualization

Generated plots:

* `data/title_length_dist.png` → Distribution of title lengths
* `data/top_sources.png` → Top news sources

---

## 📊 Visualizations

### 📌 Title Length Distribution

```
![Title Length](data/title_length_dist.png)
```

### 📌 Top News Sources

```
![Top Sources](data/top_sources.png)
```

---

## 🎯 Objective

To build an end-to-end data pipeline that transforms raw real-time data into meaningful insights through cleaning, analysis, and visualization.

---

## 💡 Future Improvements

* Add sentiment analysis (NLP)
* Integrate multiple APIs (Twitter, Reddit)
* Build an interactive dashboard (Streamlit)
* Automate pipeline execution

---
