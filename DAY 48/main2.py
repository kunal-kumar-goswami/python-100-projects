# import selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.com")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep

# 1. Setup driver
driver = webdriver.Chrome()  # ensure chromedriver is in your PATH
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# 2. Locate main cookie and store items
cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")

# 3. Convert item elements to dict of upgrade ids and prices
item_ids = [item.get_attribute("id") for item in items]

timeout = time() + 5  # check upgrades every 5 seconds
end_time = time() + (5 * 60)  # run bot for 5 minutes

while time() < end_time:
    cookie.click()

    # every 5 seconds, attempt to buy the most expensive upgrade we can afford
    if time() > timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = {}
        for price in prices:
            text = price.text
            if text:
                name, cost = text.split(" - ")
                cost = int(cost.replace(",", ""))
                item_prices[cost] = name

        # check current amount of cookies
        money_element = driver.find_element(By.ID, "money").text
        money = int(money_element.replace(",", ""))

        # find affordable upgrades
        affordable = {cost: name for cost, name in item_prices.items() if cost <= money}

        if affordable:
            highest = max(affordable)
            upgrade_id = affordable[highest].lower().replace(" ", "")
            driver.find_element(By.ID, upgrade_id).click()

        timeout = time() + 5  # reset timer

# After 5 minutes, output stats
print(driver.find_element(By.ID, "cps").text)
driver.quit()
