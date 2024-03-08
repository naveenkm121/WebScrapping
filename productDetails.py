import pandas as pd
import requests as req
import re
from bs4 import BeautifulSoup

productIdList=[]
productNameList=[]
thumbnailList=[]
imagesList=[]
discountPercList=[]
pricesList=[]
descriptionList=[]
reviewsList=[]
productLinks=[]

prodImages=[]

baseUrl="https://www.flipkart.com"
prodId=300
for i in range(2,10):
    #print(str(i))
   
    testurl="https://www.flipkart.com/search?q=mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    res= req.get(testurl)
    soup=BeautifulSoup(res.text,"html.parser")
    productsCardBox=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    # Products Name
    prodNames=productsCardBox.find_all("div",class_="_4rR01T")
    for i in prodNames:
        name=i.text
        productNameList.append(name)
        productIdList.append(prodId)
        prodId=prodId+1

    # Product Thumnails
    thumbnails=productsCardBox.find_all("img",class_="_396cs4")
    for i in thumbnails:
        name=i['src']
        thumbnailList.append(name) 

    # Products Description
    desc=productsCardBox.find_all("ul",class_="_1xgFaf")
    for i in desc:
        #description=i.text
        #print(i.prettify())
        descriptionList.append(i)  
    
    # Product Discount
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

    # Products Reviews

    reviews=productsCardBox.find_all("div",class_="_3LWZlK")
    for i in reviews:
        review=i.text
        reviewsList.append(review) 

    for pad in range(len(productNameList)-len(reviewsList)):
        reviewsList.append(4);    

    links=productsCardBox.find_all("a",class_="_1fQZEK")
    for i in links:
        review_link = i['href']
        productLinks.append(baseUrl+review_link)    

    # for prodLink in productLinks:
    #     prodRes= req.get(prodLink)
    #     prodSoup=BeautifulSoup(prodRes.text,"html.parser")
    #     images=prodSoup.find_all("img",class_="q6DClP")
    #     for img in images:
    #         prodImages.append(img["src"]) 

        
#Create DataFrame
dataframe = pd.DataFrame({
    "id": productIdList,
    "title": productNameList,
    "description": descriptionList,
    "price": pricesList,
    "discount_per": discountPercList,
    "rating": reviewsList,
    "thumbnail": thumbnailList,
    "link": productLinks
})
dataframe.to_csv("Flipkart.csv")
#print(dataframe)


# print(len(productIdList))
# print(len(productNameList))
# print(len(descriptionList))
# print(len(pricesList))
# print(len(discountPercList))
# print(len(reviewsList))
# print(len(productLinks))
# print(len(thumbnailList))