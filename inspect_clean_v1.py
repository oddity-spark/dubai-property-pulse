import pandas as pd

file_path = "data_clean/dubai_property_sales_v1.csv"

df = pd.read_csv(file_path, nrows=1000)

print("Sample shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nDate range in sample:")
print(df["instance_date"].min())
print(df["instance_date"].max())