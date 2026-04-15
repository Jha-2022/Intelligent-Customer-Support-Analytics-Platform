import pandas as pd
import joblib
import sys
import os

def run_pipeline():
    print("Loading features and target data...")
    df = pd.read_csv('data/processed/04_features_and_target.csv')
    
    print("Loading preprocessor and model...")
    preprocessor = joblib.load('models/preprocessor.pkl')
    model = joblib.load('models/churn_xgb.pkl')
    
    features = ['Recency', 'Frequency', 'Monetary', 'Tenancy', 'AvgOrderValue', 'AvgDaysBetweenOrders']
    X = df[features]
    
    print("Transforming features...")
    X_scaled = preprocessor.transform(X)
    
    print("Predicting churn probability...")
    df['Churn_Probability'] = model.predict_proba(X_scaled)[:, 1]
    
    print("Applying decision logic...")
    from src.decision_engine import apply_decision_logic
    df = apply_decision_logic(df)
    
    output_path = 'data/processed/07_customer_decisions.csv'
    print(f"Saving final decisions to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Pipeline complete!")

if __name__ == '__main__':
    run_pipeline()
