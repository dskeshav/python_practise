#Merging the dictonariers from different sources
route={'id':127,'title':'fast app'}
query={'id':1,'render_fast':True}
post={'email':'j@j.com','name':'Jeff'}

print("Individual dictionaries")
print("Route : {}".format(route))
print("Query : {}".format(query))
print("Post : {}".format(post))

# NON-pythonic
m1={}
for k in query:
    m1[k]=query[k]
for k in route:
    m1[k]=route[k]
for k in post:
    m1[k]=post[k]

#classic
m2=query.copy()
m2.update(route)
m2.update(post)

#dictionary comprehension
m3={k:v for d in [query,route,post] for k,v in d.items()  }

#Pythonic way for python>3.5 version
m4={**query,**route,**post}


print("Merged dictionary")
print(m1)
print(m2)
print(m3)
print(m4)