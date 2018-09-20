def lyrics_to_frequencies(lyrics):
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
    return myDict

def most_common_words(freqs):
    values=freqs.values()
    best=max(values)
    words=[]
    for k in freqs:
        if freqs[k]==best:
            words.append(k)
    return (words,best)

def words_often(freqs,minTimes):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freqs)
        if temp[1]>=minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done=True
    return result
def main():
    lyrics="She sells sea shells on the sea shore".split(' ')
    Dict=lyrics_to_frequencies(lyrics)
    print(Dict)
    bestWord=most_common_words(Dict)
    print(bestWord)
    print(words_often('she',5))
    filter()

if __name__=="__main__":
    main()