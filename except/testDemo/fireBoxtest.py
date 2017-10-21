from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://pan.baidu.com")

print('Before login .............')
title=driver.title
print('标题是：',title)
now_url=driver.current_url
print('当前：',now_url)
#邮箱登录
driver.find_element_by_xpath('//*[@id="login-middle"]/div/div[6]/div[2]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').clear()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('13797619091')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').clear()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').send_keys('1833738741ljl')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__submit"]').click()
time.sleep(3)
#定位页面
sreach_window=driver.current_window_handle #此行代码用来定位当前页面
time.sleep(5)
print(sreach_window)

#打开图片http://ask.csdn.net/questions/657460

driver.find_element_by_xpath('//a[@class="tulDx0R" and @href="/disk/timeline"]').click()
print("5s后加载文档")
time.sleep(5)

driver.find_element_by_xpath('//a[@class="b-no-ln" and @href="/disk/home#category/type=4"]').click()
print("2s后加载视频")
time.sleep(2)

driver.find_element_by_xpath('//a[@class="tulDx0R" and @href="#category/type=1"]').click()
print("2s后加载种子")
time.sleep(2)

driver.find_element_by_xpath('//a[@class="tulDx0R" and @href="#category/type=7"]').click()
print("返回到主页面,5s后关闭页面")

time.sleep(5)
driver.back()
print("关闭页面")
driver.quit()
'''
#打开文档
driver.find_element_by_xpath('//a[@class="tulDx0R" and @href="#category/type=4"]').click()
'''
'''http://www.w3.org/TR/css3-selectors/
http://saucelabs.com/blog/index.php/2009/10/selenium-tip-of-the-week-start-improving-your-locators/
综上所述，就是:
有固定id的用id selector， 
没有固定id的用css selector。 
Pseudo-selements ：contains（）很好用。
#首先切换到默认的frame
driver.switchTo().defaultContent();
#切换到某个frame：
driver.switchTo().frame('layoutMain');
#从一个frame切换到另一个frame：
#driver.switchTo().frame(“mainFrame”);
#切换到某个window：
#driver.switchTo().window(“windowName”);
'''





