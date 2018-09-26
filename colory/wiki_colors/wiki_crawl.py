from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import csv
from collections import OrderedDict
html_string=urlopen('https://en.wikipedia.org/wiki/List_of_colors:_N-Z').read()
soup = BS(html_string, 'lxml')
soup=soup.find_all('table')[0]
d=OrderedDict()
for row in soup.find_all('tr'):
	name=row.find_all('th')[0].get_text()
	hex_val=None
	if row.find_all('td'):
		hex_val=row.find_all('td')[0].get_text().replace('#','0x').lower()
	d[hex_val]=name
with open('wiki_colors.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in d.items():
       writer.writerow([key, value])	
		
		

		


