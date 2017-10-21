from selenium import webdriver
import selenium.webdriver.support.ui as ui
import os,time

#实现下载文件
fp=webdriver.FirefoxProfile()
print('设置目录')
fp.set_preference("browser.download.folderList",2)
print('#显示下载')
fp.set_preference("browser.download.manager.showWhenStarting",True)
print('#制定所在目录')
fp.set_preference("browser.download.dir",os.getcwd())
print('#下载文档类型')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/x-zip-compressed")
'''
driver=webdriver.Firefox(firefox_profile=fp)
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("Bootstrap")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.find_element_by_xpath("//div[@id='4']/h3/a").click()
time.sleep(60)

wait = ui.WebDriverWait(driver,60)
wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/div/p[2]/a"))
'''

driver=webdriver.Firefox(firefox_profile=fp)
driver.get("http://getbootstrap.com/2.3.2/")
driver.find_element_by_xpath("//a[@href='assets/bootstrap.zip']").click()
print("aaa")
time.sleep(20)
#退出系统
driver.quit()