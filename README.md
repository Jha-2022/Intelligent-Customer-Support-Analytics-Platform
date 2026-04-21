# Intelligent Customer Support Analytics Platform
This repository contains an end-to-end analytics platform designed to predict customer churn and automate retention strategies. By leveraging an XGBoost machine learning model and a custom decision engine, the platform identifies at-risk customers and provides actionable recovery plans to maximize revenue retention.

## Key Features
* **Machine Learning Pipeline:** Utilizes an XGBoost model to calculate churn probabilities based on customer behavior metrics like Recency, Frequency, and Monetary value.

* **Intelligent Decision Engine:** Automatically categorizes customers into Value Tiers (Low, Mid, High) and Risk Tiers (Low, Medium, High) to prescribe specific business actions.

* **Advanced Feature Engineering:** Calculates complex metrics such as ```SpendVelocity``` (tracking if a customer is slowing down) and ```UniqueItemsCount``` to better understand purchasing patterns.

* **Interactive Command Center:** A Streamlit-based dashboard providing high-level KPIs, including "Revenue at Stake" and "Average Churn Probability".

## Repository Structure

* ``app/:`` Contains the Streamlit dashboard files for data visualization.

* ``src/:`` Core logic and pipeline scripts:

  * ``run_pipeline.py:`` Orchestrates the full process from feature transformation to saving final decisions.

  * ``decision_engine.py:`` Defines the logic for risk-tiering and the business "Action Plan" matrix.

  * ``feature_engineering.py:`` Functions for generating advanced behavioral features.

* ``models/:`` Stores serialized preprocessors and trained XGBoost models (.pkl files).

* ``data/:`` Directory for raw data and processed results, specifically the final 07_customer_decisions.csv.

## Decision Matrix Logic

The system assigns actions based on the intersection of customer value and churn risk:

| Risk Tier | Value Tier | Recommended Action |
| -------- | -------- | -------- |
| High Risk | High Value | VIP Save: Personal Call + 30% Discount |
| High Risk | Low/Mid Value | Standard Save: Automated Email Discount |
| Low Risk | High Value | Loyalty: Early Access to New Designs |
| Any | Any | Monitor: Regular Newsletter |

## Getting Started


Intelligent Customer Support Analytics Platform
This repository contains an end-to-end analytics platform designed to predict customer churn and automate retention strategies. By leveraging an XGBoost machine learning model and a custom decision engine, the platform identifies at-risk customers and provides actionable recovery plans to maximize revenue retention.

Key Features
Machine Learning Pipeline: Utilizes an XGBoost model to calculate churn probabilities based on customer behavior metrics like Recency, Frequency, and Monetary value.

Intelligent Decision Engine: Automatically categorizes customers into Value Tiers (Low, Mid, High) and Risk Tiers (Low, Medium, High) to prescribe specific business actions.

Advanced Feature Engineering: Calculates complex metrics such as SpendVelocity (tracking if a customer is slowing down) and UniqueItemsCount to better understand purchasing patterns.

Interactive Command Center: A Streamlit-based dashboard providing high-level KPIs, including "Revenue at Stake" and "Average Churn Probability".

Repository Structure
app/: Contains the Streamlit dashboard files for data visualization.

src/: Core logic and pipeline scripts:

run_pipeline.py: Orchestrates the full process from feature transformation to saving final decisions.

decision_engine.py: Defines the logic for risk-tiering and the business "Action Plan" matrix.

feature_engineering.py: Functions for generating advanced behavioral features.

models/: Stores serialized preprocessors and trained XGBoost models (.pkl files).

data/: Directory for raw data and processed results, specifically the final 07_customer_decisions.csv.

Decision Matrix Logic
The system assigns actions based on the intersection of customer value and churn risk:

Risk Tier	Value Tier	Recommended Action
High Risk	High Value	VIP Save: Personal Call + 30% Discount
High Risk	Low/Mid Value	Standard Save: Automated Email Discount
Low Risk	High Value	Loyalty: Early Access to New Designs
Any	Any	Monitor: Regular Newsletter

## Getting Started

#### Prerequisites
* Python 3.x
* Dependencies: ``pandas``, ``numpy``, ``streamlit``, ``xgboost``, ``joblib``, ``scikit-learn``

#### Execution
1. **Generate Insights:** Run the main pipeline to process customer data and generate the decision file:
   ```python src/run_pipeline.py```
2. **Launch Dashboard:** Start the Streamlit application to visualize the results:
   ```
       streamlit run app/streamlit_app.py
   ```
