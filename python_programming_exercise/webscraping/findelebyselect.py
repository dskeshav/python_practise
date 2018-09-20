#find element by select method of beautiful soup

import bs4

if __name__=="__main__":
    try:
        with open('example.html') as exampleFile:
            exampleSoup=bs4.BeautifulSoup(exampleFile,features="html.parser")
            element=exampleSoup.select('#author')
            print('return Type of select method : ',type(element))
            print('Type of items in the list : ',type(element[0]))
            print("text in the enclosed tag : "+element[0].getText())
            print("attrabutes the element : ",element[0].attrs)
            print("Element : ",element)
    except FileNotFoundError as fnf:
        print("There is problem in %s"%fnf)
    #Getting paragraph element
    pElement=exampleSoup.select('p')
    print("List of all Paragraph Element: ",pElement)
    print("First paragraph Element: ",pElement[0])
    print("pElement text :"+pElement[0].getText())
    print("pElement attrs :",pElement[0].attrs)

    #Getting span element
    spanElement=exampleSoup.select('span')[0]
    print("spanElement id :"+spanElement.get('id'))
    print("spanElement attrs :",spanElement.attrs )
