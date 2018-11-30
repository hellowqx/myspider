""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/27 9:59
    @Author  : WQX
    @title   :
    
"""
import time
from selenium import webdriver
#创建浏览器对象
options=webdriver.ChromeOptions()
options.add_argument('--headless')
chrome=webdriver.Chrome(options=options)


chrome.get('http://quote.eastmoney.com/center/gridlist.html#index_sh')
prices=chrome.find_elements_by_xpath("//table[@id='main-table']/tbody/tr/td[@class=' listview-col-Close']/span")
for price in prices:

    # data=Table(price=price)
    # insert(data)
    print(price.text)


