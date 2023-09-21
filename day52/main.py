from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
USERNAME = "minhdq.22bi13276@usth.edu.vn"
PASSWORD = "Minh1611"
ACC = "cristiano"

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= options)


driver.get("https://www.instagram.com/accounts/login/")

 
username = driver.find_element(by=By.NAME, value='username')
username.send_keys(USERNAME)

password =  driver.find_element(By.NAME,"password")
password.send_keys(PASSWORD)

time.sleep(2)
password.send_keys(Keys.ENTER)
    
