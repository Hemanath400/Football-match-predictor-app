# ⚽ Football Match Outcome Predictor

A Machine Learning web application that predicts the outcome of a football match (Home Win, Draw, Away Win) using **XGBoost** and engineered match statistics. The app is built with **Streamlit** for an interactive dashboard experience.

---

## 🚀 Live Demo

*(Add Streamlit Cloud link here after deployment)*

---

## 📌 Project Overview

This project predicts football match results using historical match features such as:

* Team performance statistics
* Win rates
* Goal differences
* Recent form
* Tournament context

The model is trained using  **XGBoost Classifier** , optimized for multiclass classification.

---

## 🧠 Machine Learning Approach

* Algorithm: **XGBoost Classifier**
* Problem Type: Multiclass Classification
* Target Classes:
* 0 → Home Win
* 1 → Draw
* 2 → Away Win

---

## 📊 Features Used

* Home team encoded
* Away team encoded
* Tournament encoded
* Home win rate
* Away win rate
* Home average goals
* Away average goals
* Home form
* Away form
* Home goal difference
* Away goal difference
* Neutral venue flag
* Time features (year, month)

---

## 🖥️ Web App Features

The Streamlit dashboard includes:

### 📊 EDA Section

* Dataset overview
* Sample data preview
* Missing value analysis
* Basic statistics

### 📈 Model Insights

* Feature summary
* Correlation analysis

### 🎯 Prediction Module

* Select teams and tournament
* Predict match outcome
* View probability distribution

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib

---

## 📁 Project Structure

<pre class="overflow-visible! px-0!" data-start="1746" data-end="1993"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>football-match-predictor/</span><br/><span>│</span><br/><span>├── app.py</span><br/><span>├── requirements.txt</span><br/><span>├── README.md</span><br/><span>│</span><br/><span>├── models/</span><br/><span>│   ├── xgb_match_predictor.pkl</span><br/><span>│   ├── home_encoder.pkl</span><br/><span>│   ├── away_encoder.pkl</span><br/><span>│   └── tournament_encoder.pkl</span><br/><span>│</span><br/><span>├── data/</span><br/><span>│   └── match_features.csv</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## ⚠️ Important Note About Data

👉 **Raw dataset is NOT included in this repository.**

Only the **processed feature dataset (`match_features.csv`)** is used for:

* Model inference
* Feature extraction
* Streamlit dashboard operations

The original raw data was used only during model training and preprocessing and is not shared due to size / licensing constraints.

---

## 🧪 Model Performance

| Model       | Accuracy |
| ----------- | -------- |
| XGBoost     | ~57%     |
| Baseline ML | ~48%     |

---

## ▶️ How to Run Locally

<pre class="overflow-visible! px-0!" data-start="2543" data-end="2743"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼt"># Clone repository</span><br/><span class="ͼ10">git</span><span> clone https://github.com/your-username/football-match-predictor.git</span><br/><br/><span class="ͼt"># Install dependencies</span><br/><span>pip install </span><span class="ͼ12">-r</span><span> requirements.txt</span><br/><br/><span class="ͼt"># Run Streamlit app</span><br/><span>streamlit run app.py</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

## 📦 Installation Requirements

<pre class="overflow-visible! px-0!" data-start="2783" data-end="2841"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>streamlit</span><br/><span>pandas</span><br/><span>numpy</span><br/><span>scikit-learn</span><br/><span>xgboost</span><br/><span>joblib</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## 📌 Future Improvements

* Add real-time match API data
* Improve feature engineering
* Add deep learning model comparison
* Deploy with Docker
* Add player-level statistics

---

## 👨‍💻 Author

**Hemanath T**

Data Science & Machine Learning Enthusiast

---

## ⭐ If you like this project

Give a ⭐ on the repository and connect on LinkedIn!
