import csv
import pandas as pd
import requests as req
import re
from bs4 import BeautifulSoup

productLink=[]
images=[]
# Open the CSV file
with open('Flipkart.csv', newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Each row is a list containing the values of the cells
        # Do something with the row data, for example, print it
        # print(row)
        productLink.append(row[-1])
    
    #print(productLink)
for link in productLink:
    #testurl="https://www.flipkart.com/search?q=mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
    res= req.get(link)
    soup=BeautifulSoup(res.text,"html.parser")
    #productsCardBox=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    # Products Name
    prodNames=soup.find_all("ul",class_="_3GnUWp")
    for i in prodNames:
        name=i.find("img",class_="q6DClP").get('src')
        images.append(name)
    print(images)
