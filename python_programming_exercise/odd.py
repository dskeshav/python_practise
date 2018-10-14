from datetime import datetime
import time

odds=[1,3,5,7,9,11,13,15,17,19,21,23,258,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

for i in range(10):
    right_this_minute=datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a odd")
    else :
        print("This minute seems even")
    time.sleep(5)