#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

def main():
    MINBALANCE=500
    netAmount=0
    print("Type the transaction log")
    
    while True:
        log=input()
        if not log:
            break
        s=log.split(" ")
        print(s)
        value=s[0].upper()
        print(value)
        amount=int(s[1]) 
   
        if value=="D":
            netAmount+=amount
            print("netAmount in D",netAmount)
        elif value=="W" and netAmount>MINBALANCE:
            netAmount-=amount
            print("netAmount in W",netAmount)
        else :
            pass
    print(netAmount)


main()