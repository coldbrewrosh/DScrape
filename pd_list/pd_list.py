import csv

# Define a function to transform the URLs
def transform_url(url):
    # Replace "www.daraz.com.np/" with "https://www.daraz.com.np/"
    transformed_url = url.replace("www.daraz.com.np/", "https://www.daraz.com.np/")

    # Append the desired query parameters (e.g., ?ajax=true&page=102&sort=order)
    transformed_url += "?ajax=true&page=iterator&sort=order"

    return transformed_url

# Input and output file names
input_file = 'Categories/category_data_5.csv'
output_file = 'pd_list/output.csv'

# Open the input and output CSV files
with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # Write the header row to the output CSV
    writer.writerow(['Clothing Type', 'Transformed URL'])

    # Iterate through the rows of the input CSV
    for row in reader:
        clothing_type, original_url = row

        # Transform the URL
        transformed_url = transform_url(original_url)

        # Write the transformed data to the output CSV
        writer.writerow([clothing_type, transformed_url])

print(f"Transformation complete. The output has been saved to {output_file}")
