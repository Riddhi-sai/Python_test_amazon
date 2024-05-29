from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("https://www.amazon.in")

    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("waterbottle for office")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    assert "waterbottle for office".lower() in driver.title.lower()

        
finally:
    driver.quit()
    