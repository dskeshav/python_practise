#parse html file using the "Beautiful soup"

import bs4
import requests


if __name__=="__main__":
    res=requests.get('http://nostarch.com')
    res.raise_for_status()
    noStarchSoup=bs4.BeautifulSoup(res.text,features="html.parser")
    print(type(noStarchSoup))
    with open('example.html') as exampleFile:
        exampleSoup=bs4.BeautifulSoup(exampleFile,features="html.parser")
        print(type(exampleSoup))
