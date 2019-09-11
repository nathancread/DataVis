from bs4 import BeautifulSoup
import urllib3


def scrapeOLDER(url):
    http = urllib3.PoolManager()
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")
    newLinks = []
 

    for link in soup.find_all('a', href=True):
        if link['href'] == "/wiki/Category:People_by_time":
           print('found one')
    return newLinks

'''
def scrape(url):
    http = urllib3.PoolManager()
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")
    li = soup.find('a', {'class': 'text'})
        children = li.findChildren("a" , recursive=False)
        for child in children:
                print child
'''

def scrape2(url):
    http = urllib3.PoolManager()
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")

    links = soup.find_all('a',class_="CategoryTreeLabel  CategoryTreeLabelNs0 CategoryTreeLabelPage")
    for link in links:
        print(link)
    



#scrape('https://en.wikipedia.org/wiki/Special:CategoryTree?target=Category%3APeople&mode=all&namespaces=&title=Special%3ACategoryTree')
scrape2('https://en.wikipedia.org/wiki/Category:People_by_century')
print("dataVis")
