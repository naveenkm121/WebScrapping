import pandas as pd
import requests as req
import re
from bs4 import BeautifulSoup

productNameList=[]
imagesList=[]
discountPercList=[]
pricesList=[]
descriptionList=[]
reviewsList=[]

baseUrl="https://www.flipkart.com"

for i in range(2,10):
    testurl="https://www.flipkart.com/search?q=mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"
    res= req.get(testurl)
    soup=BeautifulSoup(res.text,"html.parser")
    productsCardBox=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    # Products Name
    prodNames=productsCardBox.find_all("div",class_="_4rR01T")
    for i in prodNames:
        name=i.text
        productNameList.append(name)

    # Products Images
    images=productsCardBox.find_all("img",class_="_396cs4")
    for i in images:
        name=i['src']
        imagesList.append(name)
    #print(imagesList)

    # Products Brands
    discountPer=productsCardBox.find_all("div",class_="_3Ay6Sb")
    for i in discountPer:
        name=i.text
        discountPercList.append(name) 

    # Products Price
    prices=productsCardBox.find_all("div",class_="_3I9_wc _27UcVY")
    for i in prices:
        # Extract text
        name_with_symbol = i.text

        # Remove the ₹ symbol using regular expression
        name_without_symbol = re.sub(r'₹', '', name_with_symbol)
        pricesList.append(name_without_symbol) 
    #print(pricesList)
        
        

    # Products Description
    desc=productsCardBox.find_all("ul",class_="_1xgFaf")
    for i in desc:
        description=i.text
        descriptionList.append(description)    

    # Products Reviews
    reviews=productsCardBox.find_all("div",class_="_3LWZlK")
    for i in reviews:
        review=i.text
        reviewsList.append(review) 

dataframe=pd.DataFrame({"title":productNameList,"description":descriptionList,"price":pricesList,"discount_per":discountPercList,"rating":reviewsList,"thumbnail":imagesList})
    #print(dataframe)
dataframe.to_csv("D:/PythonWorkSpace/flipkartData.csv")

 #   nextPage=soup.find("a",class_="_1LKTO3").get("href")
  #  fullNextPageUrl=baseUrl+nextPage
   # print(fullNextPageUrl)


