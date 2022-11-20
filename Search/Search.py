try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


"""
general resources:
List 1: food banks
List 2: Charities 

List 3: job postings in the area
List 4: career workshops in the area

academic resources:
List 5:scholarships and bursaries in that area
List 6:tutoring workshops and studying workshops

mental health resources:
List 7:Mental heath support in area
List 8:suicide helpline in the area
"""

def datafinder(country,city,num):
    queries= [
    "Food banks in  %s %s" %(country,city),
    "Charities in  %s %s" %(country,city),
    "Job postings in  %s %s" %(country,city),
    "Career workshops in  %s %s" %(country,city),
    "Scholarships and bursaries in %s %s" %(country,city),
    "Tutoring workshops and studying workshops in %s %s" %(country,city),
    "Mental health support centers in %s %s" %(country,city),
    "Suicide helpline in  %s %s" %(country,city),
    ]
    listsOfSite = []

    for x in queries:
        tempList = []
        for y in search(x,num=num,stop = num,pause =2):
            tempList.append(y)
        listsOfSite.append(tempList)
    return listsOfSite

    
data = datafinder("canada","calgary",3)

for x in data:
    print(x)
    print("------------------------------------")