# Used Car Price Analysis (CRISP-DM)

This project applies the **CRISP-DM** framework to a Kaggle used-car dataset subset (~426k rows) to identify which factors drive used-car prices and translate those into dealership recommendations.

## CRISP-DM Steps
1. **Business Understanding** — Define what “value” means to buyers and which decisions the dealership needs (acquisition, pricing, reconditioning).
2. **Data Understanding** — Explore columns, missingness, outliers, target distribution.
3. **Data Preparation** — Clean values, encode categoricals, and engineer features (age, miles/year, condition bucket, brand tier).
4. **Modeling** — Baseline Linear Regression + tree-based models (Random Forest / Gradient Boosting).
5. **Evaluation** — Compare MAE/RMSE/R²; use permutation importance / SHAP for interpretability.
6. **Deployment** — Convert insights into an inventory & pricing playbook.

## How to run locally
1. Put the dataset CSV in `data/` as `used_cars.csv` (do **not** commit the large CSV to Git).
2. Open `notebooks/01_eda.ipynb` and run all cells (creates a cleaned parquet).
3. Open `notebooks/02_modeling.ipynb` and run all cells (trains model, exports importances).
4. Read the final write-up in `reports/report.md`.

## Data
This analysis uses a Kaggle “Used Cars” dataset (original ~3M rows; subset ~426k).  
Please download from Kaggle directly and place it as `data/used_cars.csv` locally.

## Repo structure
