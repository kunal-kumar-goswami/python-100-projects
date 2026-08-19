from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(option = chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_page")

article_count = driver.find_element(value="#article  a" )
print(article_count.text)


