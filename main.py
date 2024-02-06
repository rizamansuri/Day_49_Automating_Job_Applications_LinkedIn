import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# to leave browser opened after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3823155509&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# Automatic login to linkedin
sign_in_btn = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_btn.click()

# Input username
username = driver.find_element(By.CSS_SELECTOR, value="form #username")
username.send_keys(os.environ.get("USERNAME"))

# Input password
password = driver.find_element(By.CSS_SELECTOR, value="form #password")
password.send_keys(os.environ.get("PASSWORD"))

# Click on the sign in button
sign_in_btn2 = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_in_btn2.click()


time.sleep(2)
# Apply automatically
easy_apply_btn = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply_btn.click()

mobile_number = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3823155509-111429186-phoneNumber-nationalNumber"]')
if mobile_number.text == "":
    mobile_number.send_keys("1234567890")
# driver.close()
submit_btn = driver.find_element(By.CSS_SELECTOR, value="footer button")
submit_btn.click()


# Even after this submit button you may get next button according to job post....