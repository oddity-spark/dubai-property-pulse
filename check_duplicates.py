import pandas as pd

file_path = "data_clean/dubai_property_sales_v1.csv"

df = pd.read_csv(file_path)

print("Total rows:")
print(len(df))

print("\nUnique transaction_id:")
print(df["transaction_id"].nunique())

print("\nDuplicate transaction_id rows:")
print(len(df) - df["transaction_id"].nunique())

print("\nMost repeated transaction IDs:")
print(df["transaction_id"].value_counts().head(10))

print("\nRows for top repeated transaction:")
top_id = df["transaction_id"].value_counts().index[0]
print(df[df["transaction_id"] == top_id].head(20))