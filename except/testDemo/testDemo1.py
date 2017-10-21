from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.126.com")
driver.switch_to_frame('x-URS-iframe')  #需先跳转到iframe框架
username=driver.find_element_by_name('email')
username.clear()
username.send_keys("13797619091")

password=driver.find_element_by_name("password")
password.clear()
password.send_keys("123456789ljl")

dologin=driver.find_element_by_id("dologin")
dologin.click()