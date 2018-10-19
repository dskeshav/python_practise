#program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number


def main():
    print("Enter a series of number seperated by ',' ")
    try:
        series=input()
        numList=series.split(",")
        numTuples=tuple(numList)
        print(numList)
        print(numTuples)
    
    except ValueError:
        print("Invalid entry.")
        main()

main()