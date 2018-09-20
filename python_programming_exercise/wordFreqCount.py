#Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
import os
def main():
    print("Type a sentence whose word frequency is to be determined")
    freq={}
    line=input()
    for word in line.split():
        freq[word]=freq.get(word,0)+1

    words =freq.keys()
    words.sort()

    for w in words:
        print("%s:%d" % (w,freq[w]))

def getFileName():
    return os.__doc__

if __name__=='__main__':
    print("name doc: ",__name__.__doc__)
    # print(getFileName())
    # main()