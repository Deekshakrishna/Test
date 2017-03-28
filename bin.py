import urllib2
from bs4 import BeautifulSoup



wiki = "https://www.thebalance.com/corporate-tax-rates-and-tax-calculation-397647?utm_term=find+tables&utm_content=p1-main-3-title&utm_medium=sem&utm_source=google_s&utm_campaign=adid-aec6427d-1900-4513-912c-de9ddad63f5b-0-ab_gsb_ocode-4567&ad=semD&an=google_s&am=broad&q=find+tables&o=4567&qsrc=999&l=sem&askid=aec6427d-1900-4513-912c-de9ddad63f5b-0-ab_gsb"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,'html.parser')
rows = soup.find_all('tr')
for row in rows:
    row1 = row.find_all("td")
    for col in row1:
        print col.text
#row1 = rows.find("td")
#rows.contents
#print rows
#for row in rows
#print row1
