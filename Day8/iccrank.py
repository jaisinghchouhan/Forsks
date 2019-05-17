import requests
from bs4 import BeautifulSoup
source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
#print(source)
soup = BeautifulSoup(source,"lxml")
right_tables=soup.find('table',class_='table')
print (right_tables)
a=[]
b=[]
c=[]
d=[]
e=[]
print(soup.table.tbody.tr)
for row in right_tables.findAll('tr'):
    cells = row.findAll('td')
    if len(cells)==5:
        print(cells)
        a.append(cells[0].text.strip())
        b.append(cells[1].text.strip())
        c.append(cells[2].text.strip())
        d.append(cells[3].text.strip())
        e.append(cells[4].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ["pos","team","weighted matches","points","rating"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")