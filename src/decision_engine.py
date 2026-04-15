import pandas as pd
import numpy as np

def apply_decision_logic(customer_df):
    # Define Tiers based on Quantiles
    customer_df['Value_Tier'] = pd.qcut(customer_df['Monetary'], 3, labels=['Low Value', 'Mid Value', 'High Value'])
    
    # Define Risk based on Churn Probability
    def get_risk_tier(prob):
        if prob > 0.7: return 'High Risk'
        if prob > 0.3: return 'Medium Risk'
        return 'Low Risk'
    
    customer_df['Risk_Tier'] = customer_df['Churn_Probability'].apply(get_risk_tier)
    
    # Decision Matrix
    def get_action(row):
        if row['Risk_Tier'] == 'High Risk' and row['Value_Tier'] == 'High Value':
            return 'VIP Save: Personal Call + 30% Discount'
        if row['Risk_Tier'] == 'High Risk':
            return 'Standard Save: Automated Email Discount'
        if row['Risk_Tier'] == 'Low Risk' and row['Value_Tier'] == 'High Value':
            return 'Loyalty: Early Access to New Designs'
        return 'Monitor: Regular Newsletter'

    customer_df['Action_Plan'] = customer_df.apply(get_action, axis=1)
    return customer_df

# Save result
# final_df = apply_decision_logic(customer_df)
# final_df.to_csv('../data/processed/07_customer_decisions.csv', index=False)