#download web page from requests module

import requests

if __name__=="__main__":
    res=requests.get("https://automatetheboringstuff.com/files/rj.txt")
    try:
        res.raise_for_status()
    except Exception as exc:
        print("There is a problem %s"%(exc))
    else:
        print("else block")
    finally:
        print(res.status_code)
