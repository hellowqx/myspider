""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/27 9:11
    @Author  : WQX
    @title   :
    
"""

import time

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument('--headless')

chrome=webdriver.Chrome(options=options)

chrome.get('https://image.baidu.com/')
myinput=chrome.find_element_by_id('kw')
a=input('请输入搜索内容')
myinput.send_keys(a)
btn=chrome.find_element_by_class_name('s_search')
btn.click()
time.sleep(2)
js='var a=document.documentElement.scrollTop=2000'
chrome.execute_script(js)
chrome.save_screenshot('img/14.png')
chrome.close()
chrome.quit()


[scrapy.spidermiddlewares.offsite] DEBUG: Filtered offsite request to 'www.111.com.cn': <GET https://www.111.com.cn/categories/965143>

DEBUG: Redirecting (302) to <GET https://www.111.com.cn/errorpage.html> from <GET https://www.111.c
om.cn/robots.txt>
li id="producteg_780552">\n             '>]
【下单立减40元】汇仁 肾宝片 0.7g*126片
                        322.0
scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (302) to <GET https://www.111.com.cn/errorpage.html> from <GET https://www.111.c
om.cn/robots.txt>


scrapy.DEBUG: Retrying (failed 1 times): [<twis ted.python.failure.Failure twisted.internet.error.ConnectionDone: Connection was closed cleanly.>]