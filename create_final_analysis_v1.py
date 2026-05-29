import pandas as pd
from pathlib import Path

input_file = "data_clean/dubai_property_sales_v1.csv"
output_file = Path("data_clean/final_area_quarter_analysis_v1.csv")

df = pd.read_csv(input_file)

# Find top 30 communities by total transaction volume
top_areas = (
    df["area_name_en"]
    .value_counts()
    .head(30)
    .index
)

df_top = df[df["area_name_en"].isin(top_areas)].copy()

# Base quarterly metrics
base = (
    df_top.groupby(["area_name_en", "quarter"])
    .agg(
        transaction_count=("transaction_id", "count"),
        median_transaction_value=("actual_worth", "median"),
        median_price_per_sqm=("meter_sale_price", "median"),
        total_transaction_value=("actual_worth", "sum"),
        median_area_sqm=("procedure_area", "median"),
    )
    .reset_index()
)

# Off-plan / ready counts
reg_counts = (
    df_top.groupby(["area_name_en", "quarter", "reg_type_en"])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)

reg_counts = reg_counts.rename(
    columns={
        "Off-Plan Properties": "off_plan_count",
        "Existing Properties": "ready_count",
    }
)

if "off_plan_count" not in reg_counts.columns:
    reg_counts["off_plan_count"] = 0

if "ready_count" not in reg_counts.columns:
    reg_counts["ready_count"] = 0

final = base.merge(reg_counts, on=["area_name_en", "quarter"], how="left")

final["off_plan_count"] = final["off_plan_count"].fillna(0)
final["ready_count"] = final["ready_count"].fillna(0)

final["off_plan_share"] = final["off_plan_count"] / final["transaction_count"]
final["ready_share"] = final["ready_count"] / final["transaction_count"]

# Sort before calculating QoQ growth
final = final.sort_values(["area_name_en", "quarter"])

final["qoq_transaction_growth"] = (
    final.groupby("area_name_en")["transaction_count"]
    .pct_change()
)

final["qoq_price_growth"] = (
    final.groupby("area_name_en")["median_price_per_sqm"]
    .pct_change()
)

final.to_csv(output_file, index=False)

print("Final analysis file created:")
print(output_file)

print("\nRows and columns:")
print(final.shape)

print("\nFirst 10 rows:")
print(final.head(10))

print("\nColumns:")
print(final.columns.tolist())