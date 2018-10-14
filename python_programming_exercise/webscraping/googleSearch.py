import sys
import webbrowser

import bs4
import requests

if __name__=="__main__":
    searchText=" ".join(sys.argv[1:])
    res=requests.get("http://google.com/search?q="+searchText)
    res.raise_for_status()
    soupText=bs4.BeautifulSoup(res.text,features="html.parser")
    linkElems=soupText.select('.r a')
    numOpen=min(5,len(linkElems))
    print(numOpen)
    print(linkElems)
    # webbrowser.Chrome.open()
    for i in range(numOpen):
        webbrowser.get('chrome %s').open_new_tab("https://google.com" + linkElems[i].get('href'))
