from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from credentials import get_email, get_password, get_phone_num
import time

my_email = get_email()
my_password = get_password()
my_phone_num = get_phone_num()

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&geoId=103644278&keywords=python%20intern&location=United%20States")

time.sleep(1)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(my_email)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(my_password)
password_field.send_keys(Keys.ENTER)

time.sleep(2)

job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in job_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(3)
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(my_phone_num)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            # skip complex applications
            continue

        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("Skipped due to lack of apply button")
        continue

time.sleep(5)
driver.quit()