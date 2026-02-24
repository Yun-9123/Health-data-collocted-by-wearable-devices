import pandas as pd

# Read csv file
file_path = "D:\OJO\coding\Health-data-collocted-by-wearable-devices\data\wearable_health_devices_performance_upto_26june2025.csv"
df = pd.read_csv(file_path)
print("Suceeded!")

# show all column name
print("\n------ Column name ------")
print(df.columns)

# show first five rows
print("\n------ First five rows ------")
print(df.head())

# show dataset info
print("\n------ info ------")
print(df.info())

# shape of data
print("\n------ shape ------")
rows, cols = df.shape
print(f"This data contained {rows}, and {cols} feature columns")

# show all column
print("\n------ columns ------")
print(df.columns.tolist())

# Statistic abstract
print("\n------ statistic info ------")
print(df.describe())


