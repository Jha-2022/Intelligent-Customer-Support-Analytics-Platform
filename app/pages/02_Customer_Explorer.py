import streamlit as st
import pandas as pd

st.title("🔍 Individual Customer Explorer")

df = pd.read_csv("data/processed/07_customer_decisions.csv")

customer_id = st.number_input("Enter Customer ID", min_value=int(df['Customer ID'].min()), max_value=int(df['Customer ID'].max()))

if st.button("Analyze Customer"):
    user_data = df[df['Customer ID'] == customer_id]
    
    if not user_data.empty:
        row = user_data.iloc[0]
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Churn Probability", f"{row['Churn_Probability']*100:.1f}%")
            st.write(f"**Segment:** {row['Segment']}")
        with c2:
            st.metric("Total Spend", f"${row['Monetary']:,.2f}")
            st.write(f"**Recommended Action:** :red[{row['Action_Plan']}]")
            
        st.divider()
        st.write("### Behavior Profile")
        st.progress(row['Churn_Probability'], text="Churn Risk Score")
        st.write(f"- **Recency:** {row['Recency']} days since last purchase.")
        st.write(f"- **Frequency:** {row['Frequency']} total orders.")
    else:
        st.warning("Customer ID not found in database.")