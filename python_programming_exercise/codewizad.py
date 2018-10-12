import sys

namedByList=()



for i in sys.argv[1:]:
    namedByList+="".join(i)

print(len(namedByList))