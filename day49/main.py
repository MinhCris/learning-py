from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= options)

driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

account = driver.find_element(By.ID,"username")
account.send_keys("minhdq1611@gmail.com")

password = driver.find_element(By.ID,"password")
password.send_keys("@Minh1611")
password.send_keys(Keys.ENTER)

time.sleep(10)

apply_button = driver.find_element(By.XPATH,'//a[@class="app-aware-link  global-nav__primary-link"][@href="https://www.linkedin.com/jobs/?"]')
apply_button.click()
time.sleep(5)
 
PHONE = "0979701611"
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()