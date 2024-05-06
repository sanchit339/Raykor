import pandas as pd

file_path = 'Data.txt'
records = []

with open(file_path, 'r') as file:
    for line in file:
        records.append(line.strip())

df = pd.DataFrame(records, columns=['data'])

df.to_parquet('new_data.parquet', index=False)

print("Data has been written to 'output.parquet'")
