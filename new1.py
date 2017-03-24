#import urllib2
#filehandle= urllib.urlopen("http://www.google.com")
#crisp= urllib2.urlopen(filehandle)
#soup = BeautifulSoup(crisp)
#print soup.prettify()

#from bs4 import BeautifulSoup
#import urllib2

#googleFile = urllib2.urlopen("http://www.google.com")
#googleHtml = googleFile.read()
#googleFile.close()

#soup = BeautifulSoup(googleHtml)
#googleAll = soup.find_all("a")
#for links in soup.find_all('a'):
    #print (links.get('href'))


import urllib2
from bs4 import BeautifulSoup
were = "https://www.google.com"

page = urllib2.urlopen(were)
soup = BeautifulSoup(page)
print soup.prettify()
