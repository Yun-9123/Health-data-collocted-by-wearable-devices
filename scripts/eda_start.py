import pandas as pd

# Read csv file
file_path = "D:\OJO\coding\Health-data-collocted-by-wearable-devices\data\wearable_health_devices_performance_upto_26june2025.csv"
df = pd.read_csv(file_path)
print("Suceeded!")

# show all column name
print("------ Column name ------")
print(df.columns)

# show first five rows
print("------ First five rows ------")
print(df.head())

# show dataset info
print("------ info ------")
print(df.info())


