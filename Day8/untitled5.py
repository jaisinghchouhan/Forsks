# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:58:27 2019

@author: ck069
"""
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

import sqlite3

conn = sqlite3.connect ( 'db_university.db' )
co = conn.cursor()

co.execute ("""CREATE TABLE icc(
          pos TEXT, 
          team TEXT, 
          matches TEXT, 
          points TEXT,
         rating TEXT
            )""") 
#co.execute("DROP TABLE icc")
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
for i in range(0,10):
    co.execute('INSERT INTO icc(pos,team,matches,points,rating) VALUES(?, ?,?,?,?)',
                 (a[i],b[i],c[i],d[i],e[i]))       
    #c.execute("INSERT INTO icc VALUES ("+a[i]+","+b[i]+","+c[i]+","+d[i]+","+d[i]+")")
#co.commit()    
co.execute("SELECT * FROM icc")

df=DataFrame(co.fetchall())
df.columns=["pos","team","matches","ponits","rating"]


