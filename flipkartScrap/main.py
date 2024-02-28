import pandas as pd
import requests 
from bs4 import BeautifulSoup

product_name = []
price = []
Description = []
reviews = []
title = input("enter your product = ").replace(" ","+")

for i in range(2,4):
    url = f"https://www.flipkart.com/search?q={title}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    

    soup = BeautifulSoup(r.text, "lxml")
    # print(soup)
    box = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")
    # np(next_page)
    # np = soup.find()

    names = box.find_all("div",class_ ="_4rR01T")
    # print(names)
    for i in names:
        name = i.text
        product_name.append(name)
#     print(product_name)

    prices = box.find_all("div",class_ ="_30jeq3 _1_WHN1")
    for i in prices:
        name=i.text.replace("₹","").replace(",","")
        price.append(name)
#     print(price)
    
    description = box.find_all("ul",class_ ="_1xgFaf")
    for i in description:
        name=i.text
        Description.append(name)
#     print(Description)

    Reviews = box.find_all("div",class_ = "_3LWZlK")
    for i in Reviews :
        name =i.text
        reviews.append(name)
#     print(len(reviews))
df =pd.DataFrame({"Product Names": product_name,"Prices": price, "Descriptions": Description})
print(len(product_name),len(price), len(description), len(reviews) )
df.to_csv(f"{title}.csv")
print("done")