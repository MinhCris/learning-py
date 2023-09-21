from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/minh/Downloads/chrome-mac-arm64"
driver = webdriver.Chrome( )

driver.get("https://www.python.org/")
# price =driver.find_element(By.ID,"productTitle")
# print(price.text)

search_bar = driver.find_element(By.NAME,"q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME,"python-logo")

documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH,"")


#find_element("id", "taxInclusiveMessage") 