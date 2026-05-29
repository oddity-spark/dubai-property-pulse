import pandas as pd

file_path = "data_raw/transactions_2026-05-26_02-03-11_2.csv.gz"

df_sample = pd.read_csv(file_path, compression="gzip", nrows=1000)

print("Sample rows and columns:")
print(df_sample.shape)

print("\nColumn names:")
print(df_sample.columns.tolist())

print("\nDate range in sample:")
print(df_sample["instance_date"].min())
print(df_sample["instance_date"].max())

print("\nTransaction group values:")
print(df_sample["trans_group_en"].value_counts(dropna=False))

print("\nUsage values:")
print(df_sample["property_usage_en"].value_counts(dropna=False))

print("\nProperty type values:")
print(df_sample["property_type_en"].value_counts(dropna=False))

print("\nProperty subtype values:")
print(df_sample["property_sub_type_en"].value_counts(dropna=False).head(20))

print("\nRegistration type values:")
print(df_sample["reg_type_en"].value_counts(dropna=False))

print("\nTop 20 areas:")
print(df_sample["area_name_en"].value_counts(dropna=False).head(20))