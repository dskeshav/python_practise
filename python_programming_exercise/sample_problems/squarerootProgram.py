# program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
import math

def main():
    C=50;H=30
    print("Enter a series of number where a expressions squarerooot is to be calculated")
    series=input()
    serlist=str(series).split(",")
    Q=[str(round(math.sqrt((2*C*float(D))/H),2)) for D in serlist if (str(D).isdigit())]
    print(",".join(Q))


main()
