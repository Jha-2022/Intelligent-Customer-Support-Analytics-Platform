# Intelligent Customer Support Analytics Platform
This repository contains an end-to-end analytics platform designed to predict customer churn and automate retention strategies. By leveraging an XGBoost machine learning model and a custom decision engine, the platform identifies at-risk customers and provides actionable recovery plans to maximize revenue retention.

## Key Features
* **Machine Learning Pipeline:** Utilizes an XGBoost model to calculate churn probabilities based on customer behavior metrics like Recency, Frequency, and Monetary value.

* **Intelligent Decision Engine:** Automatically categorizes customers into Value Tiers (Low, Mid, High) and Risk Tiers (Low, Medium, High) to prescribe specific business actions.

* **Advanced Feature Engineering:** Calculates complex metrics such as ```SpendVelocity``` (tracking if a customer is slowing down) and ```UniqueItemsCount``` to better understand purchasing patterns.

* **Interactive Command Center:** A Streamlit-based dashboard providing high-level KPIs, including "Revenue at Stake" and "Average Churn Probability".
