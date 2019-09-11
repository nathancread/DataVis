from bs4 import BeautifulSoup
import certifi
import urllib3

url = 'https://en.wikipedia.org//wiki/Jules_Aarons'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())    
req = http.request('GET',url)
page = req.data.decode('utf-8')
soup = BeautifulSoup(page.data,features="html.parser")