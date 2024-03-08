import pandas as pd
import requests as req
import re
from bs4 import BeautifulSoup

prodIds=[]
productImages=[]





df = pd.read_csv('Flipkart.csv', usecols=['id', 'link'])

# Iterate over rows and print values of column 1 and column 2
for index, row in df.iterrows():
    # Access values of column 1 and column 2 for each row
    prodId = row['id']
    prodLink = row['link']
    res= req.get(prodLink)
    soup=BeautifulSoup(res.text,"html.parser")
    images=soup.find_all("img",class_="q6DClP")
    for image in images:
        productImages.append(image["src"])
        prodIds.append(prodId)


dataframe = pd.DataFrame({
    "prod_id": prodIds,
    "src": productImages,
})    

dataframe.to_csv("FlipkartProdImages.csv")