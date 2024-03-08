import pandas as pd
import pandas as pd
import requests as req
import re
from bs4 import BeautifulSoup

productImages=[]
testurl="https://www.flipkart.com/motorola-g54-5g-mint-green-128-gb/p/itmfc12683043bbc?pid=MOBGQFX8Z3ZCDZZ7&lid=LSTMOBGQFX8Z3ZCDZZ7FOOELB&marketplace=FLIPKART&q=mobile+&store=tyy%2F4io&srno=s_2_25&otracker=search&otracker1=search&iid=61778787-0253-4756-a0aa-4ceba052f943.MOBGQFX8Z3ZCDZZ7.SEARCH&ssid=98o6ozn18g0000001709919350131&qH=179b063c26bcaa74";
res= req.get(testurl)
print(res)
soup=BeautifulSoup(res.text,"html.parser")
productName=soup.find("span",class_="B_NuCI")
images=soup.find_all("img",class_="q6DClP")
#print(images)
for image in images:
    productImages.append(image["src"])

print(productImages)