from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Create a Selenium WebDriver instance
driver = webdriver.Chrome()

# Open the URL of the reviews section
url = "https://www.daraz.com.np/products/shangrila-100-cotton-pack-of-4-t-shirt-for-men-black-blue-grey-white-fashion-t-shirt-for-men-i105140899-s1026788288.html?spm=a2a0e.searchlistcategory.sku.2.6d005d448mOhpp&search=1"
driver.get(url)

# Initialize a CSV file for writing
csv_file = open(r'D:\System\Desktop\reviews.csv', 'w', newline='', encoding='utf-8')

# csv_file = open('D:\System\Desktop\reviews.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write the header row to the CSV file
csv_writer.writerow(["Ratings", "User", "Review", "Image 1", "Image 2", "Image 3", "Image 4", "SKU", "Helpful"])

# Wait for the element with class "mod-reviews" to be present (adjust timeout as needed)
wait = WebDriverWait(driver, 20)  # Adjust the timeout as needed
reviews_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mod-reviews")))


# Find the root element that contains the reviews
root_element = driver.find_element_by_class_name("mod-reviews")

# Find all review items within the root element
review_items = root_element.find_elements_by_class_name("item")


for review_item in review_items:
    # Extract the rating (count the number of stars)
    rating_element = review_item.find_elements_by_class_name("container-star starCtn left")
    rating_img = rating_element.get_attribute("src")
    if rating_img == "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png":
        ratings = ratings + "•"
    
    # Extract user, review, and SKU information
    user = review_item.find_element_by_class_name("middle").text
    review = review_item.find_element_by_class_name("content").text
    sku_info = review_item.find_element_by_class_name("skuInfo").text

    # Extract review images
    # review_images = review_item.find_elements_by_class_name("image")
    # image_links = [image.get_attribute("style").split('"')[1] for image in review_images]

    # Extract helpful count
    helpful = review_item.find_element_by_class_name("lazadaicon.great").text

    # Write the data to the CSV file
    # csv_writer.writerow([ratings, user, review, image_links[0], image_links[1], image_links[2], image_links[3], sku_info, helpful])

    csv_writer.writerow([ratings, user, review, sku_info, helpful])
    
# Close the CSV file
csv_file.close()

# Close the Selenium WebDriver
driver.quit()