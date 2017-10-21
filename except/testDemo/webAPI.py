from selenium import webdriver
driver=webdriver.Firefox()
print("WebDriver属于selenium体系中设计出来操作浏览器的一套API，webDriver是Python的一个用于实现web自动话的第三方方库")
#定位元素：自动化做的就是模拟鼠标键盘操作组件元素，单击，输入，悬停等
#webDriver就是通过前段工具找到的元素信息找到不同元素
#webDriver定位方法：ID，class name ,link text,xpath ,find_element_by_id(),find_element_by_class_name(),find_element_by_link_text(),find_element_by_xpath()
#通过ID
driver.find_element_by_id()
#通过name
driver.find_element_by_name()
#通过class
driver.find_element_by_class_name()
#通过Tag
driver.fint_element_by_tag_name()
#通过Link转成用来定位文本链接<a>
driver.find_element_by_link_text()
#通过partial link
driver.find_element_by_partial_link_text()
#http://blog.csdn.net/mrlevo520/article/details/51954203定位数据还未加载完成时
#通过XPath绝对路径定位（层级关系】）
driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[4]/h3/a")
#元素属性
driver.find_element_by_xpath("//*[@id='1']")
driver.find_element_by_xpath("//input[@name='1']")
driver.find_element_by_xpath("//input[@class='1']")
driver.find_element_by_xpath("//*[@class='1']")
#层级与属性结合
driver.find_element_by_xpath("//span[@class='bg s_ipt_wr']/input")
#使用逻辑运算符and
driver.finf_element_by_xpath("//input[@id='kw' and @class='su']/span/input")
#使用css定位（.class）(#id)(*)(element)(element>element)(element+element)([attribute=value])
driver.find_element_by_css_selector(".class")
driver.find_element_by_css_selector("#id")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("span>input")
driver.find_element_by_css_selector("[autocomplete=off]")
driver.find_element_by_css_selector("[name='kw']")
driver.find_element_by_css_selector("[type='submit']")

#控制浏览器
#窗口大小（set_window_size()）
#后退前进（back(),forward()）
#浏览器刷新（refresh()）
driver.clear()
driver.send_keys("*value")
driver.click()