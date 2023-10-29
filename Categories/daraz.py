import csv
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# # Your HTML snippet
# html_code = """
#     <a href="//www.daraz.com.np/womens-sarees/">
#     <img src="//laz-img-cdn.alicdn.com/images/ims-web/TB11DyxpNYaK1RjSZFnXXa80pXa.jpg" alt="Saree" class="catCircleImg">
#     <span>Saree</span></a></li><li class="lzd-site-menu-grand-item">
#     <a href="//www.daraz.com.np/womens-shalwar-kameez/">
#     <img src="//laz-img-cdn.alicdn.com/images/ims-web/TB1K4CppMHqK1RjSZFkXXX.WFXa.jpg" alt="Kurtas" class="catCircleImg">
#     <span>Kurtas</span></a></li>
#     <!-- More items... -->
# """

# Specify the path to your HTML file
html_file_path = 'D:\System\Desktop\daraz2.html'
csv_file_path = 'D:\System\Desktop\category_data_5.csv'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <a> elements containing category information
category_elements = soup.find_all('a')

# Initialize a list to store category data
category_data = []


# Extract category names and URLs, excluding items with "javascript:void(0)" in the URL
for category in category_elements:
    category_name = category.find('span').get_text()
    
    # Check if the 'href' attribute exists and if it's not equal to "javascript:void(0)"
    if 'href' in category.attrs and category['href'] != 'javascript:void(0)':
        category_url = category['href']
        
        # Parse the URL and reconstruct it to remove everything after the last '/'
        parsed_url = urlparse(category_url)
        new_category_url = f"{parsed_url.scheme}{parsed_url.netloc}{parsed_url.path}"

        category_data.append([category_name, new_category_url])

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Category Name', 'URL'])  # Write header
    csv_writer.writerows(category_data)

print(f'Data has been saved to {csv_file_path}')