import pandas as pd

# Define the prefix and suffix for your CSV file names
prefix = "pd_list_req/csv/mens-casual-tops-page-"
suffix = ".csv"

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through the file numbers from 1 to 102
for file_number in range(1, 11):
    # Construct the file name based on the prefix and suffix
    file_name = f"{prefix}{file_number}{suffix}"
    
    try:
        # Read the CSV file and store it in the list
        data = pd.read_csv(file_name)
        data_frames.append(data)
        print(f"Read {len(data)} rows from {file_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping.")

# Concatenate the DataFrames into one
merged_data = pd.concat(data_frames, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('merged_data.csv', index=False)
print(f"Total rows in merged DataFrame: {len(merged_data)}")