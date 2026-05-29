import pandas as pd
from pathlib import Path

input_file = "data_raw/transactions_2026-05-26_02-03-11_2.csv.gz"
output_file = Path("data_clean/dubai_property_sales_v1.csv")

chunksize = 100_000
clean_chunks = []

columns_needed = [
    "transaction_id",
    "instance_date",
    "trans_group_en",
    "procedure_name_en",
    "reg_type_en",
    "property_usage_en",
    "property_type_en",
    "property_sub_type_en",
    "area_name_en",
    "project_name_en",
    "rooms_en",
    "procedure_area",
    "actual_worth",
    "meter_sale_price",
]

for chunk in pd.read_csv(
    input_file,
    compression="gzip",
    usecols=columns_needed,
    chunksize=chunksize,
):
    chunk["instance_date"] = pd.to_datetime(chunk["instance_date"], errors="coerce")

    filtered = chunk[
        (chunk["instance_date"] >= "2023-01-01")
        & (chunk["trans_group_en"] == "Sales")
        & (chunk["property_usage_en"] == "Residential")
        & (chunk["property_type_en"] == "Unit")
        & (chunk["property_sub_type_en"] == "Flat")
        & (chunk["actual_worth"].notna())
        & (chunk["procedure_area"].notna())
        & (chunk["procedure_area"] > 0)
    ].copy()

    clean_chunks.append(filtered)

clean_df = pd.concat(clean_chunks, ignore_index=True)

clean_df = clean_df.drop_duplicates(subset=["transaction_id"])
print(f"\nRows after deduplication: {len(clean_df)}")

clean_df["year"] = clean_df["instance_date"].dt.year
clean_df["quarter"] = clean_df["instance_date"].dt.to_period("Q").astype(str)
clean_df.to_csv(output_file, index=False)

print("Clean file created:")
print(output_file)

print("\nRows and columns:")
print(clean_df.shape)

print("\nDate range:")
print(clean_df["instance_date"].min())
print(clean_df["instance_date"].max())

print("\nRegistration type values:")
print(clean_df["reg_type_en"].value_counts(dropna=False))

print("\nTop 20 areas:")
print(clean_df["area_name_en"].value_counts().head(20))
