from selenium import webdriver # 导入webdriver包
import time
# 初始化一个火狐浏览器实例：driver
driver = webdriver.Chrome()

# 最大化浏览器
driver.maximize_window()

# 通过get()方法，打开一个url站点
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
print ("运行结束，5秒后关闭页面")
time.sleep(5)
driver.quit()


