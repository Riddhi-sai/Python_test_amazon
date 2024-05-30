from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
from urllib.parse import urlparse, urlunparse, ParseResult


driver = webdriver.Chrome()

try:
    driver.get("https://www.amazon.in")

    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("waterbottle for office")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    assert "waterbottle for office".lower() in driver.title.lower()
    print("Test Passed 1")

    # Filtering the search results: The test should filter the search results by price range and
    # verify that the filtered results are displayed correctly.

    min_range = driver.find_element(By.NAME, "low-price")
    max_range = driver.find_element(By.NAME, "high-price")

    min_price = 300
    max_price = 1000
    driver.execute_script(
        f"arguments[0].setAttribute('value', '{min_price}')", min_range)

    driver.execute_script(
        f"arguments[0].setAttribute('value', '{max_price}')", max_range)

    # click go
    go_btn = driver.find_element(By.CLASS_NAME, "a-button-input")
    go_btn.click()

    time.sleep(5)

    results = driver.find_elements(By.CLASS_NAME, "a-price-whole")

    for res in results:
        price = int(res.text.replace(',', ''))
        # print(price)
        assert price <= max_price and price >= min_price
    time.sleep(10)
    print("Test Passed 2")

    products = driver.find_elements(
        By.XPATH, '//a[@class="a-link-normal s-no-outline"]')
    product = products[4]
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    product.click()

    # Wait for the new window or tab to be opened
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    original_window = driver.current_window_handle

    # Switch to the new window or tab
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    variation_divs = driver.find_elements(
        By.CSS_SELECTOR, "div[id^='variation_']")  # ?
    for variation in variation_divs:
        ul_element = variation.find_element(By.TAG_NAME, "ul")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        if len(li_elements) >= 2:
            li_elements[1].click()
        else:
            print(
                f"No second option available for {variation.get_attribute('id')}")

    product_id = li_elements[1].get_attribute('data-csa-c-item-id')
    # print(product_id)
    time.sleep(5)

    # add_to_cart_btn = driver.find_element(By.ID,"add-to-cart-button")
    add_to_cart_btn = driver.find_element(
        By.XPATH, "//input[@id='add-to-cart-button']")
    driver.execute_script("arguments[0].click();", add_to_cart_btn)

    cart_count_element = driver.find_element(By.ID, "nav-cart-count")
    cart_count_value = cart_count_element.text
    assert cart_count_value == "1"
    print("Test Passed 3")

    cart_link = driver.find_element(By.ID, "nav-cart")
    cart_link.click()
    print('cart clicked')

    time.sleep(20)

    cart_product = driver.find_element(
        By.XPATH, '//div[@class="a-row sc-list-item sc-java-remote-feature"]')
    cart_product_id = cart_product.get_attribute('data-asin')

    if product_id in cart_product_id:
        assert True
    else:
        assert False
    print("Test Passed 4")

    # assert driver.find_element('xpath','/html/body/div[1]/div[1]/div[4]/div[5]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[3]/ul/li/span/a/span[1]/span/span[2]').text==product_text

    proceed_to_checkout_button = driver.find_element(
        By.NAME, 'proceedToRetailCheckout')
    proceed_to_checkout_button.click()
    print('checkout clicked')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ap_email")))
    email_or_phone_input_box = driver.find_element(By.ID, 'ap_email')
    email_or_phone_input_box.send_keys("9041975002")
    email_or_phone_input_box.send_keys(Keys.RETURN)

    password_input_box = driver.find_element(By.ID, 'ap_password')
    password_input_box.send_keys('Rid_12345')
    password_input_box.send_keys(Keys.RETURN)

    # print('Clicked signin')

    select_address_btn = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.ID, "shipToThisAddressButton")))
    select_address_btn.click()

    # print('address seleted')

    time.sleep(15)

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"pp-7TYaC8-97")))
    radio_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='radio' and @value='SelectableAddCreditCard']")))
    radio_button.click()
    # print("Radio button selected successfully!")
    # card_payment_selection = driver.find_element(By.XPATH,'pp-7TYaC8-97')
    # card_payment_selection.click()
    time.sleep(10)

    enter_details_select = driver.find_element(
        By.XPATH, "//a[@class='a-link-emphasis pmts-add-cc-default-trigger-link']")
    enter_details_select.click()
    print('details clicked')

   # Locate the shadow host element to enter the payment detail
   # the following shows an error while locaitng the element.
    '''shadow_host = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "grammarly-desktop-integration"))
    )
    # Execute JavaScript to access the shadow root
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    # Locate the credit card input field within the shadow root
    card_number_field = shadow_root.find_element(By.XPATH, "//input[@name='addCreditCardNumber']']")
    # Enter the credit card number
    card_number_field.send_keys("5425233430109903")

    print("Test Passed 5")'''
    time.sleep(30)
finally:
    driver.quit()