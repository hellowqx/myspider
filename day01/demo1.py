from urllib import request
import urllib

# url='https://www.sina.com.cn/'
#
# a=request.urlopen(url)
# print(dir(a))
# html=a.read()
# print(html.decode('utf-8'))
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__path__', '__spec__', 'error', 'parse',
 'request', 'response']


# my_header={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
# import chardet
# url=request.Request('https://www.csdn.net/',headers=my_header)
# print(dir(url))
#
#
# response=request.urlopen(url).read()
# encodeing=chardet.detect(response).get('encoding')
# print(response.decode(encodeing,errors='ignore'))

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_data', '_full_url', '_parse', '_tunnel_host', 'add_header',
 'add_unredirected_header', 'data', 'fragment', 'full_url', 'get_full_url', 'get_header',
 'get_method', 'has_header', 'has_proxy', 'header_items', 'headers', 'host', 'origin_req_host',
 'remove_header', 'selector', 'set_proxy', 'type', 'unredirected_hdrs', 'unverifiable']



from fake_useragent import UserAgent
import chardet
import random
ua=UserAgent()



req= request.Request('https://www.sina.com.cn/')
req.add_header('User-Agent',ua.random)

response=request.urlopen(req)
html=response.read()
encodeing=chardet.detect(html).get('encoding')

print(html.decode(encodeing))