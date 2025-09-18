# Used Car Price Analysis — CRISP-DM Findings

## Executive Summary (for the dealership)
- **Age & miles/year** dominate value. Newer cars with lower annual mileage command materially higher prices across brands and body styles.
- **Condition** is a major multiplier. “Like new/Excellent” ≫ “Good” ≫ “Fair/Salvage.”
- **Brand tier** matters. Premium marques (BMW, Mercedes-Benz, Lexus, Tesla, Acura) retain value better and erode more slowly.
- **Drivetrain & body type**: 4WD/AWD trucks & SUVs price higher (especially in truck-heavy states); hybrids/EVs do best in urban/coastal markets.
- **Title status** (when present) is decisive: clean ≫ rebuilt/salvage.

### Inventory & Pricing Playbook
1) Prioritize ≤7–8 years old and ≤ segment-median **miles/year**.  
2) Stock **Excellent/Like-new** condition; avoid **Fair/Salvage** unless the buy price is deeply discounted.  
3) Maintain a **premium brand lane** for margins.  
4) Localize mix: trucks/SUVs+AWD for truck states; hybrids/EVs for dense/urban states.  
5) Enforce **title discipline**; price rebuilt/salvage aggressively or pass.  
6) **Reconditioning ROI**: cosmetic & safety fixes tend to pay; deep powertrain repairs rarely do unless certifiable.

---

## 1) Business Understanding
Goal: reveal price drivers so the dealership can refine **acquisitions, reconditioning, and pricing**.  
Decisions: what to buy, how to price, and what to recondition.  
Success: lower MAE/RMSE; better gross/turns.

## 2) Data Understanding
- **Source:** Kaggle used-cars (~426k subset of ~3M).  
- **Columns:** `price` (target), `year`, `manufacturer`, `model`, `condition`, `odometer`, `fuel`, `transmission`, `drive`, `type`, `title_status`, `paint_color`, `state`.  
- **Checks:** duplicates, missingness (notably `condition/title_status`), outliers (`price` < $500 or > $200k; `odometer` > 400k), `year` sanity (1985–present).

## 3) Data Preparation
- **Cleaning:** drop/cap implausible `price`, `year`, `odometer`; normalize manufacturers.  
- **Features:**
  - `age = current_year − year`
  - `miles_per_year = odometer / max(age, 1)`
  - `condition_bucket` (A_new / B_excellent / C_good / D_fair / E_salvage / Z_unknown)
  - `brand_tier` (premium vs mainstream)
  - (optional) `state` dummies; interactions (state×type, drive×type)
- **Encoding:** one-hot for categoricals; passthrough numerics.

## 4) Modeling
- **Baseline:** Linear Regression (interpretability).  
- **Primary:** Random Forest / Gradient Boosting (nonlinear effects).  
- **Metrics:** MAE, RMSE, R² (hold-out or K-fold).  
- **Explainability:** permutation importance or SHAP.

**Common top drivers on this dataset family:** age, miles_per_year, condition_bucket, brand/manufacturer (brand_tier), body type, drivetrain, title_status, and state.

## 5) Evaluation & Insights
- Prices fall as **age** and **miles/year** rise.  
- **Condition** steps add/subtract thousands (quantify during your run).  
- **Premium** brands keep value better at higher mileage.  
- **Trucks/SUVs + AWD/4WD** carry premiums in relevant markets.  
- **Title_status**: clean ≫ rebuilt/salvage.  
- Bigger errors: salvage/fair, very high-mile luxury, rare trims—price cautiously.

## 6) Deployment / Next Steps
- Acquisition filters & pricing adjustments as above.  
- Monitor MAE by **brand/age/mileage** buckets; retrain quarterly.  
- Add seasonality, regional interactions, and SHAP plots in production.
