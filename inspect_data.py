import pandas as pd

file_path = "data_raw/transactions-2026-05-27.csv"

df = pd.read_csv(file_path)

print("Rows and columns:")
print(df.shape)

print("\nDate range:")
print(df["INSTANCE_DATE"].min())
print(df["INSTANCE_DATE"].max())

print("\nUSAGE_EN values:")
print(df["USAGE_EN"].value_counts(dropna=False))

print("\nPROP_TYPE_EN values:")
print(df["PROP_TYPE_EN"].value_counts(dropna=False))

print("\nPROP_SB_TYPE_EN values:")
print(df["PROP_SB_TYPE_EN"].value_counts(dropna=False).head(20))

print("\nIS_OFFPLAN_EN values:")
print(df["IS_OFFPLAN_EN"].value_counts(dropna=False))

print("\nTop 20 areas:")
print(df["AREA_EN"].value_counts(dropna=False).head(20))
