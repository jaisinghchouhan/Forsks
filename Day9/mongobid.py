from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

import pymongo

client = pymongo.MongoClient("mongodb://jaisingh:jaisingh%40123@cluster0-shard-00-00-ht9pp.mongodb.net:27017,cluster0-shard-00-01-ht9pp.mongodb.net:27017,cluster0-shard-00-02-ht9pp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=client.employee
#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://bidplus.gem.gov.in/bidlists"


browser = webdriver.Chrome("F:\Forsk\Day9\chromedriver_win32\chromedriver.exe")
browser.get(url)


sleep(2)

A=[]
B=[]
C=[]
D=[]

for i in range(1,11):
    A.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[1]/p[1]/a").text)    
    B.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[1]/span").text)
    C.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[2]/span").text)
    D.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[3]/p[2]").text)
    

sleep(5)
  
def add_employee(A,B,C,D):
    for i in range (0,10):
        mydb.employees.insert_one(
                {
                "nane" : A[i],
                "age" : B[i],
                "rollno" : C[i],
                "branch" : D[i]
                })
        return "Employee added successfully"
 
def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)
    
fetch_all_employee()



html_page = browser.page_source

soup = BS(html_page)



sleep(3)


browser.quit()

