import requests
from bs4 import BeautifulSoup
import time

time.localtime()

request=requests.get("http://www.google.com")

print(request.content)
print("Hello")
print(time.localtime())