from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(option = chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(value="fName")
last_name = driver.find_element(value="lName")
email = driver.find_element(value="email")

first_name.send_keys("King")
last_name.send_keys("Kong")
email.send_keys("king@email.com")

submit = driver.find_element(value="form button")
submit.click()