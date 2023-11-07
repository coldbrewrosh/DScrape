import csv

# Define a function to generate 102 links for each category
def generate_links(category, num_links=102):
    base_url = f"https://www.daraz.com.np/{category}?ajax=true&page="
    links = [base_url + str(page) + "&sort=order" for page in range(1, num_links + 1)]
    return links

# Input and output file names
input_file = 'Categories/category_data_5.csv'
output_file = 'pd_list/output_all.csv'

# Open the input and output CSV files
with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # Iterate through the rows of the input CSV
    for row in reader:
        clothing_type, original_url = row

        # Generate 102 links for each category
        links = generate_links(original_url)

        # Write the transformed data to the output CSV without the "Clothing Type" column
        for link in links:
            writer.writerow([link])

print(f"Transformation complete. The output has been saved to {output_file}")
