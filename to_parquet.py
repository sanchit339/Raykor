import pandas as pd

# Path to your dataset
file_path = 'Dat.txt'

# Initialize a list to hold each record as a single string
records = []

# Read the dataset line by line
with open(file_path, 'r') as file:
    for line in file:
        records.append(line.strip())

# Convert list to DataFrame with a single column named 'data'
df = pd.DataFrame(records, columns=['data'])

# Save the DataFrame as a Parquet file
df.to_parquet('new_data.parquet', index=False)

print("Data has been written to 'output.parquet'")
