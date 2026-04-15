import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Customer Intelligence Pro", layout="wide")

@st.cache_data
def load_data():
    # Loading the final decisions file from Stage 2
    path = "data/processed/07_customer_decisions.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return None

st.title("🎯 Customer Retention Command Center")
st.markdown("""
Welcome to the **Customer Intelligence Dashboard**. This tool uses an **XGBoost Machine Learning model** to predict churn risk and prioritize business actions for your store.
""")

df = load_data()

if df is not None:
    # Top Level KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", f"{len(df):,}")
    col2.metric("At Risk", f"{len(df[df['Risk_Tier'] == 'High Risk']):,}")
    col3.metric("Revenue at Stake", f"${df[df['Risk_Tier'] == 'High Risk']['Monetary'].sum():,.0f}")
    col4.metric("Avg. Churn Prob.", f"{df['Churn_Probability'].mean()*100:.1f}%")

    st.info("👈 Use the sidebar to navigate to specific insights or the Action Center.")
else:
    st.error("Data file not found. Please run Stage 2 scripts first to generate '07_customer_decisions.csv'.")