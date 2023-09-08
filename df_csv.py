import pandas as pd

csv_file_path = 'Data.CSV'

df=pd.read_csv(csv_file_path)

print(df.head())
