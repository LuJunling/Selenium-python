from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://pan.baidu.com")
'''
size=driver.find_element_by_id("kw").size
print(size)
driver.quit()

#鼠标事件(ActionChains类)
#
driver.perform()#执行所有ActionChains中存储的行为
driver.context_click()#右击
driver.double_click()#双击
driver.drag_and_drop()#拖动
driver.move_to_element()#鼠标悬停
'''
driver.find_element_by_xpath('//*[@id="login-middle"]/div/div[6]/div[2]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').clear()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('13797619091')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').clear()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').send_keys('1833738741ljl')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__submit"]').click()
driver.find_element_by_css_selector('a[href*="/disk/timeline"]').click()
#layoutAside > div > div > ul.fOHAbxb > li:nth-child(2) > a
#li.zqevDYQV:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)

#鼠标右键-查看-略缩图
#driver.find_element_by_xpath('#layoutMain > div > div > div.OjL8sBUa > div > div.zJMtAEb > div').context_click()


#driver.find_element_by_xpath('//*[@id="i029849011179667406"]').move_to_element()
#driver.find_element_by_xpath('//*[@id="i016194919300006583"]').click()
