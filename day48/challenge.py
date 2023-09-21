from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

acc =driver.find_element(By.NAME,"fName")
acc.send_keys("Python")

password =driver.find_element(By.NAME,"lName")
password.send_keys('haha')

mail =driver.find_element(By.NAME,"email")
mail.send_keys("minhdq1611@gmail.com")

button = driver.find_element(By.CSS_SELECTOR,"form button")
button.click()

# search.send_keys(Keys.ENTER)