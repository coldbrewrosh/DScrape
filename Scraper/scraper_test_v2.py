from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a Selenium WebDriver instance
driver = webdriver.Chrome()

# Open the URL of the reviews section
url = "https://www.daraz.com.np/products/shangrila-100-cotton-pack-of-4-t-shirt-for-men-black-blue-grey-white-fashion-t-shirt-for-men-i105140899-s1026788288.html?spm=a2a0e.searchlistcategory.sku.2.6d005d448mOhpp&search=1"
driver.get(url)

# Scroll down to load additional elements (adjust the number of scrolls as needed)
scroll_count = 5
for _ in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "item")))

# Initialize a CSV file for writing
csv_file = open(r'D:\System\Desktop\reviews.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write the header row to the CSV file
csv_writer.writerow(["Product Name","Ratings", "Customer", "Review", "Image 1", "Image 2", "Image 3", "Image 4", "SKU", "Helpful"])

# Wait for the "mod-reviews" element to be present
# wait = WebDriverWait(driver, 10)
# reviews_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mod-reviews")))

product_name = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title").text

# Find the root element that contains the reviews using XPath
root_element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]')

# Find all review items within the root element using XPath
review_items = root_element.find_elements(By.XPATH, "//div[contains(@class, 'item')]")

for review_item in review_items:
    # Extract the rating (count the number of stars)
    rating_elements = review_item.find_elements(By.XPATH, ".//div[contains(@class, 'container-star starCtn left')]")
    ratings = "test"  # Initialize an empty string for ratings

    for rating_element in rating_elements:
        rating_img = rating_element.get_attribute("src")
        if rating_img == "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png":
            ratings = "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"
        else:
            ratings = "Blank"


    # Extract user, review, and SKU information using XPath
    # user = review_item.find_element(By.XPATH, ".//div[contains(@class, 'middle')]").text
    # review = review_item.find_element(By.XPATH, ".//div[contains(@class, 'content')]").text
    # sku_info = review_item.find_element(By.XPATH, ".//div[contains(@class, 'skuInfo')]").text

    # Extract review images using XPath
    # review_images = review_item.find_elements(By.XPATH, ".//div[contains(@class, 'image')]")
    # image_links = [image.get_attribute("style").split('"')[1] for image in review_images]

    # Extract helpful count
    # helpful = review_item.find_element(By.XPATH, ".//span[contains(@class, 'lazadaicon.great')]").text

    # Write the data to the CSV file
    # csv_writer.writerow([ratings, user, review, image_links[0], image_links[1], image_links[2], image_links[3], sku_info, helpful])
    # csv_writer.writerow([ratings, user, review, sku_info, helpful])
    csv_writer.writerow([product_name, ratings])
# Close the CSV file
csv_file.close()

# Close the Selenium WebDriver
driver.quit()
