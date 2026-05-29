import pandas as pd
from pathlib import Path

input_file = "data_clean/dubai_property_sales_v1.csv"
output_file = Path("data_clean/area_quarter_summary_v1.csv")

df = pd.read_csv(input_file)

summary = (
    df.groupby(["area_name_en", "quarter", "reg_type_en"])
    .agg(
        transaction_count=("transaction_id", "count"),
        median_transaction_value=("actual_worth", "median"),
        median_price_per_sqm=("meter_sale_price", "median"),
        total_transaction_value=("actual_worth", "sum"),
        median_area_sqm=("procedure_area", "median"),
    )
    .reset_index()
)

summary = summary.sort_values(["area_name_en", "quarter", "reg_type_en"])

summary.to_csv(output_file, index=False)

print("Summary file created:")
print(output_file)

print("\nRows and columns:")
print(summary.shape)

print("\nFirst 10 rows:")
print(summary.head(10))

print("\nTop areas by total transactions:")
print(df["area_name_en"].value_counts().head(20))
