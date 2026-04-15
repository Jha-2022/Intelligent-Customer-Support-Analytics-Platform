import streamlit as st
import pandas as pd

st.title("🚀 Action Center")
st.subheader("High-Priority Retention Targets")

# Load data again (Streamlit sharing cache)
df = pd.read_csv("data/processed/07_customer_decisions.csv")

# Sidebar Filters
st.sidebar.header("Filter Criteria")
selected_risk = st.sidebar.multiselect("Risk Level", options=df['Risk_Tier'].unique(), default=['High Risk'])
selected_value = st.sidebar.multiselect("Value Tier", options=df['Value_Tier'].unique(), default=['High Value'])

# Filter DataFrame
filtered_df = df[(df['Risk_Tier'].isin(selected_risk)) & (df['Value_Tier'].isin(selected_value))]

st.write(f"Showing {len(filtered_df)} customers matching criteria.")

# Display the Actionable Table
display_cols = ['Customer ID', 'Risk_Tier', 'Value_Tier', 'Churn_Probability', 'Action_Plan', 'Monetary']
st.dataframe(filtered_df[display_cols].sort_values(by='Churn_Probability', ascending=False), use_container_width=True)

# Export Feature
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Action List for Marketing", data=csv, file_name="marketing_action_list.csv", mime="text/csv")