import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Football AI Dashboard",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Football AI Pro Dashboard")

df = pd.read_csv("data/processed/match_features.csv")

model = joblib.load("models/xgb_match_predictor.pkl")
home_encoder = joblib.load("models/home_encoder.pkl")
away_encoder = joblib.load("models/away_encoder.pkl")
tournament_encoder = joblib.load("models/tournament_encoder.pkl")

tab1, tab2, tab3 = st.tabs(["📊 EDA", "🧠 Model Insights", "🎯 Predict"])


with tab1:

    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Matches", len(df))
    col2.metric("Teams", df["home_team"].nunique())
    col3.metric("Tournaments", df["tournament"].nunique())

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            df["home_team"].value_counts().head(10),
            title="Top Home Teams"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            df,
            x="home_win_rate",
            title="Home Win Rate Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Raw Data")
    st.dataframe(df.head())

with tab2:

    st.subheader("Model Performance Insights")

    try:
        feature_importance = model.feature_importances_

        features = [
            "home_team_enc",
            "away_team_enc",
            "tournament_enc",
            "neutral",
            "year",
            "month",
            "home_win_rate",
            "away_win_rate",
            "home_avg_goals",
            "away_avg_goals",
            "home_form",
            "away_form",
            "home_goal_diff",
            "away_goal_diff"
        ]

        fi_df = pd.DataFrame({
            "Feature": features,
            "Importance": feature_importance
        }).sort_values(by="Importance", ascending=True)

        fig = px.bar(
            fi_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Feature Importance (XGBoost)"
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error("Feature importance not available")

with tab3:

    st.subheader("Match Prediction Engine ⚽")

    teams = sorted(set(df["home_team"]) | set(df["away_team"]))
    tournaments = sorted(df["tournament"].unique())

    col1, col2, col3 = st.columns(3)

    with col1:
        home_team = st.selectbox("Home Team", teams)

    with col2:
        away_team = st.selectbox("Away Team", teams)

    with col3:
        tournament = st.selectbox("Tournament", tournaments)

    neutral = st.checkbox("Neutral Venue")

    if st.button("Predict Outcome 🚀"):

        home_enc = home_encoder.transform([home_team])[0]
        away_enc = away_encoder.transform([away_team])[0]
        tourn_enc = tournament_encoder.transform([tournament])[0]

        home_row = df[df["home_team"] == home_team].iloc[-1]
        away_row = df[df["away_team"] == away_team].iloc[-1]

        input_df = pd.DataFrame({
            "home_team_enc": [home_enc],
            "away_team_enc": [away_enc],
            "tournament_enc": [tourn_enc],
            "neutral": [int(neutral)],
            "year": [2026],
            "month": [6],
            "home_win_rate": [home_row["home_win_rate"]],
            "away_win_rate": [away_row["away_win_rate"]],
            "home_avg_goals": [home_row["home_avg_goals"]],
            "away_avg_goals": [away_row["away_avg_goals"]],
            "home_form": [home_row["home_form"]],
            "away_form": [away_row["away_form"]],
            "home_goal_diff": [home_row["home_goal_diff"]],
            "away_goal_diff": [away_row["away_goal_diff"]],
        })

        pred = model.predict(input_df)[0]
        probs = model.predict_proba(input_df)[0]

        st.subheader("Prediction Result")

        if pred == 0:
            st.success("🏠 Home Win")
        elif pred == 1:
            st.info("🤝 Draw")
        else:
            st.warning("✈️ Away Win")

        prob_df = pd.DataFrame({
            "Outcome": ["Home", "Draw", "Away"],
            "Probability": probs
        })

        fig = px.bar(
            prob_df,
            x="Outcome",
            y="Probability",
            color="Outcome",
            title="Prediction Confidence"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Gauge (confidence)
        confidence = max(probs)

        fig2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=confidence * 100,
            title={'text': "Confidence %"},
            gauge={'axis': {'range': [0, 100]}}
        ))

        st.plotly_chart(fig2, use_container_width=True)