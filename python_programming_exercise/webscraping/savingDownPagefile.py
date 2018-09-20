#save the downlaoded webpage into a file

import requests

if __name__=="__main__":
    res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    with open('RomeoJuliet.txt','wb') as playFile:
        for chunk in res.iter_content(len(res.text)):
            playFile.write(chunk)
