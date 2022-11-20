try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


"""
general resources:
List 0: food banks
List 1: Charities 

Job resources:
List 2: job postings in the area
List 3: career workshops in the area

academic resources:
List 4:scholarships and bursaries in that area
List 5:tutoring workshops and studying workshops

mental health resources:
List 6:Mental heath support in area
List 7:suicide helpline in the area


Input: 
    country: country of the user
    city:city of user
    num: number of links output per query
Outputs:
    A list of lists.
    Content of each list is as above
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

