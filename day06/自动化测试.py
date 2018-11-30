# from selenium import webdriver
# import time
# #初始化无界面选项
# options=webdriver.ChromeOptions()
# options.add_argument('--headless')
# #创建谷歌浏览器对象
# chrome =webdriver.Chrome(options=options)
#
# chrome.get('https://www.baidu.com')
# #获取输入框
# input_box=chrome.find_element_by_id('kw')
# #模拟输入数据
# input_box.send_keys('王庆祥')
# chrome.save_screenshot('info1.png')
# #获取搜素按钮
# btn=chrome.find_element_by_id('su')
# btn.click()
# time.sleep(1)
# chrome.save_screenshot('info2.png')
# # chrome.save_screenshot('baidu1.png')
# chrome.close()
# chrome.quit()
#
#
#

import time
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('--headless')
chrome=webdriver.Chrome(options=options)