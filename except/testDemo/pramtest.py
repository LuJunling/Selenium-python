from selenium import webdriver
import time

search_text=['python','中文','text']

for text in search_text:
    driver =webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("kw").send_keys(text)
    print(text)
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()