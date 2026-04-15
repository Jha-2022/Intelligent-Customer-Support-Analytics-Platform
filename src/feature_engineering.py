import pandas as pd
import numpy as np

def create_advanced_features(df, customer_df, snapshot_date):
    # 1. Trend Features: Spend in last 90 days vs total
    ninety_days_ago = snapshot_date - pd.Timedelta(days=90)
    recent_spend = df[df['InvoiceDate'] >= ninety_days_ago].groupby('Customer ID')['TotalAmount'].sum()
    
    customer_df = customer_df.merge(recent_spend, on='Customer ID', how='left').rename(columns={'TotalAmount_y': 'RecentSpend'})
    customer_df['RecentSpend'] = customer_df['RecentSpend'].fillna(0)
    
    # 2. Spend Ratio (Are they slowing down?)
    customer_df['SpendVelocity'] = customer_df['RecentSpend'] / (customer_df['Monetary'] / (customer_df['Tenancy']/30 + 1))
    
    # 3. Variety Feature
    unique_items = df.groupby('Customer ID')['StockCode'].nunique().reset_index()
    unique_items.columns = ['Customer ID', 'UniqueItemsCount']
    customer_df = customer_df.merge(unique_items, on='Customer ID', how='left')
    
    return customer_df

# Usage
# customer_df = create_advanced_features(df, customer_df, snapshot_date)