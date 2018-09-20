# """program to find number divisible by 7 and not by 5 between 2000 and 3200 """
def main():
    l=[]
    for number in range(2000,3201):
        if (number%7==0 and number%5!=0):
            l.append(str(number))

    print(','.join(l))

main()
