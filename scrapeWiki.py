from bs4 import BeautifulSoup
import certifi
import urllib3
import re
print("solid")


## TODO clean data in various ways
# fix issue with varable sized tables (issac newton wont show up) - should at least double my dataset ooof
# fix issue with random russian showing up
# fix issue with a different table being found first

## TODO finish project
#get coordinates from locatoins
# turn into pandas dataframe
#figure out how to graph this lol
#render end project into a GIF 
#post on reddit 
#get laid
def getListOfUrlStubs(url,firstEntry,lastEntry):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())    
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")
    
    newLinks = []
    going = False 

    for link in soup.find_all('a', href=True):
        if link['href'] == firstEntry:
            going = True 
            #print('became true')
        if (going == True) and ('/wiki/') in link['href']:
           newLinks.append(link['href'])
           if link['href'] == lastEntry:
               going = False
    return newLinks

def getUrls(stublist):
    for i in range (0,len(stublist)):
        stublist[i] = "https://en.wikipedia.org/" + stublist[i]
    return stublist

def scrapeNameLocDobHits(url):
    #acess website
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())    
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")
    #gives error messages lol
    
    #find the table off of a wiki page
    myTable = soup.find('table')
    #row that contains DOB and LOC
    goodRow = myTable.find_all('tr')[2]
    birthPlaceTag = goodRow.find('div')
    birthdayTag = goodRow.find('span')
    #print(birthdayTag)
    #row that contains name
    nameRow = myTable.find_all('tr')[0]
    nameTag = nameRow.find('div')
    #print(nameTag.text.decode('utf-8'))
    #retuns name, birthplace, birthday
    try:

        hits = scrapePageHits(url)
    except:
        print('unable to get hits')

    return nameTag.text,birthPlaceTag.text,birthdayTag.text, hits




def writeList(listOfPhysicists):
    with open('D:/PythonStuff/DataVis/DataList.txt','r+',encoding ='utf-8') as myFile:
        for physicist in listOfPhysicists:

            try:
                name,loc,date,hits = scrapeNameLocDobHits(physicist)
                date = str(date)[1:-1]
                hits = str(hits)
                mystr = physicist + ".,." + name +".,."+ loc +".,."+date + ".,." + hits + "\n"
                myFile.write(mystr)
                print('wrote', mystr)
            except:
                print("no infobox for this guy")


def scrapePageHits(url):
    newUrl = url[8:]#cuts out https//:
    newUrl = re.sub('en.wikipedia.org//wiki/' ,'en.wikipedia.org/',newUrl) #formats
    newUrl = re.sub("[\(\[].*?[\)\]]", "", newUrl) #cuts out weird parenthasis
    #newUrl = re.sub('(scientist)','',newUrl)
    newUrl = 'https://xtools.wmflabs.org/articleinfo/' + newUrl
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())    
    response = http.request('GET',newUrl)
    soup = BeautifulSoup(response.data,features="html.parser")
    
    myTable = soup.find('table')
    goodRow = myTable.find_all('tr')[6]
    goodCol = goodRow.find_all('td')[1]
    return int(goodCol.text)

    


listOfPhysicists = (getUrls(getListOfUrlStubs('https://en.wikipedia.org/wiki/List_of_physicists','/wiki/Jules_Aarons','/wiki/Barton_Zwiebach')))
writeList(listOfPhysicists)
#scrapePageHits(listOfPhysicists[0])
#print(scrapeNameLocDob('https://en.wikipedia.org//wiki/Jules_Aarons'))
print("completed the task")

