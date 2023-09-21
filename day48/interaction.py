from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.CSS_SELECTOR,"#articlecount a ")
# number.click()

search =driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


