
# For Mobile
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options


from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import TimeoutException


# For General Scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import csv
# import time


mobile_emulation = {
    "deviceMetrics": {"width": 428, "height": 926, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
}
# mobile_emulation = { "deviceName": "iPhone 12 Pro" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options) #sometimes you have to insert your execution path


# Open the URL of the reviews section
# url = "https://www.daraz.com.np/products/shangrila-100-cotton-pack-of-4-t-shirt-for-men-black-blue-grey-white-fashion-t-shirt-for-men-i105140899-s1026788288.html?spm=a2a0e.searchlistcategory.sku.2.6d005d448mOhpp&search=1"
url = "https://www.daraz.com.np/products/mamaearth-ubtan-face-wash-100-ml-i100764018-s1021228047.html?spm=a2a0e.searchlist.list.7.30f064c6atZEG1&search=1"
driver.get(url)

# scroll_distance = 100  # Adjust the distance you want to scroll (in pixels)
# scroll_delay = 0.1  # Adjust the delay between scrolls (in seconds)

# # Scroll down gradually
# for _ in range(20):  # Adjust the number of times you want to scroll
#     print("Scrolling...")
#     driver.execute_script("window.scrollBy(0, " + str(scroll_distance) + ");")
#     time.sleep(scroll_delay)  # Use the time.sleep function

# # Debugging: Check if the element is visible
# try:
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pdp-review-container pdp-section')))
#     print("Element found.")
# except TimeoutException:
#     print("Element not found within the specified timeout")




# # Scroll down to load additional elements (adjust the number of scrolls as needed)
# scroll_count = 1
# for _ in range(scroll_count):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="module_review"]/div/div/div[2]/div[1]/p')))



# Initialize a CSV file for writing
csv_file = open(r'D:\System\Desktop\DScrape\Scraper\productdetails.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Write the header row to the CSV file
csv_writer.writerow(["Product Name", "Product Price", "Original Price", "Discount %", "Total Sales", "Total Added to Cart","Total Wishlist", "Customer ID", "Review Date","Reviews"])

na_placeholder = "N/A"

# Product Info
product_name = driver.find_element(By.CLASS_NAME, "pdp-mod-product-title").text

product_price_raw = driver.find_element(By.CLASS_NAME, 'pdp-price').text
product_price = ''.join(char for char in product_price_raw if char.isdigit())

try:
    original_price_raw = driver.find_element(By.CLASS_NAME, 'price-discount').text
    original_price = ''.join(char for char in original_price_raw if char.isdigit())
    if original_price_raw == "":
        original_price = product_price
except NoSuchElementException:
    original_price = product_price

try:
    discount_perct = driver.find_element(By.CLASS_NAME, 'price-decrease').text
    if discount_perct == "":
        discount_perct = na_placeholder
except NoSuchElementException:
    discount_perct = na_placeholder
try:
    total_sales = driver.find_element(By.CLASS_NAME, 'product-info-sold').text
except NoSuchElementException:
    total_sales = na_placeholder

try:
    cart_added_raw = driver.find_element(By.CSS_SELECTOR, '#fomo-banner > div > div > div > div > div:nth-child(3) > div > span.normal-text').text
    cart_added = ''.join(char for char in cart_added_raw if char.isdigit())
except NoSuchElementException:
    cart_added = na_placeholder

try:
    wishlist_added_raw = driver.find_element(By.CLASS_NAME, 'pdp-mod-wishlist').text
    wishlist_added = ''.join(char for char in wishlist_added_raw if char.isdigit())
except NoSuchElementException:
    wishlist_added = na_placeholder


csv_writer.writerow([product_name, product_price, original_price, discount_perct, total_sales, cart_added, wishlist_added])

# Close the CSV file
csv_file.close()

# Close the Selenium WebDriver
driver.quit()

# Specification Loop
# Find the ul element with the specified class
# ul = driver.find_element(By.CLASS_NAME, 'specification-keys')

# Find all the li elements within the ul
# li_category = ul.find_elements(By.CLASS_NAME, 'key-title').text


# for li in li_category:
    

# # Review Loop
# for i in range(1, 6):
#     # Construct the XPath with the iteration variable i
#     rewview_date_xpath = '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[' + str(i) + ']/div[1]/span'
#     review_text_xpath = '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[' + str(i) + ']/div[3]/div[1]'
#     customer_id_xpath = '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[' + str(i) + ']/div[2]/span'
#     # Find the element using the constructed XPath
#     review_date = driver.find_element(By.XPATH, rewview_date_xpath).text
#     review_text = driver.find_element(By.XPATH, review_text_xpath).text
#     customer_id = driver.find_element(By.XPATH, customer_id_xpath).text
#     csv_writer.writerow([product_name, product_price, discounted_price, customer_id, review_date, review_text])






















# Find the root element that contains the reviews using XPath
# root_element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]')

# # Find all review items within the root element using XPath
# review_items = root_element.find_elements(By.XPATH, "//div[contains(@class, 'item')]")

# for review_item in review_items:
#     # Extract the rating (count the number of stars)
#     rating_elements = review_item.find_elements(By.XPATH, ".//div[contains(@class, 'container-star starCtn left')]")
#     ratings = "test"  # Initialize an empty string for ratings

#     for rating_element in rating_elements:
#         rating_img = rating_element.get_attribute("src")
#         if rating_img == "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png":
#             ratings = "//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"
#         else:
#             ratings = "Blank"


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
    # csv_writer.writerow([product_name, ratings])

