try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")



def datafinder(country,city,num):
    queryScolorShip = "Scholoarships in %s %s"%(country,city)
    queryMentalHealth = "Mental health support centers in %s %s"%(country,city)

    listsOfSite = [[],[],[]]

    for x in search(queryScolorShip,num=num,stop=num,pause=2):
        listsOfSite[0].append(x)
    for y in search(queryMentalHealth,num=num,stop=num,pause=2):
        listsOfSite[1].append(y)

    return listsOfSite

    
data = datafinder("canada","calgary",10)

print("scholorship")
for x in data[0]:
    print(x)

print("Mental health")
for x in data[1]:
    print(x)