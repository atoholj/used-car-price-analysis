import pandas as pd
import numpy as np

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip().str.lower()
        .str.replace(" ", "_").str.replace("-", "_")
    )
    return df

def basic_filters(df: pd.DataFrame, price_col: str = "price") -> pd.DataFrame:
    df = df.copy()
    if price_col in df:
        df = df[df[price_col].between(500, 200000, inclusive="both")]
    if "year" in df:
        df = df[df["year"].between(1985, 2025, inclusive="both")]
    if "odometer" in df:
        df = df[df["odometer"].between(0, 400000, inclusive="both")]
    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "year" in df:
        df["age"] = 2025 - df["year"]
    if {"odometer","age"}.issubset(df.columns):
        df["miles_per_year"] = df["odometer"] / np.where(df["age"]>0, df["age"], 1)
    if "condition" in df:
        df["condition_bucket"] = (
            df["condition"].astype(str).str.lower().map({
                "new": "A_new",
                "like new": "A_new",
                "excellent": "B_excellent",
                "good": "C_good",
                "fair": "D_fair",
                "salvage": "E_salvage"
            }).fillna("Z_unknown")
        )
    if "manufacturer" in df:
        premium = {"bmw","audi","mercedes_benz","mercedes-benz","lexus",
                   "acura","infiniti","volvo","porsche","tesla","cadillac","lincoln"}
        manuf_norm = df["manufacturer"].astype(str).str.lower().str.replace(" ", "_").str.replace("-", "_")
        df["brand_tier"] = np.where(manuf_norm.isin(premium), "premium", "mainstream")
    return df
