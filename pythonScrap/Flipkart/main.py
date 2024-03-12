import pandas as pd
import requests 
from bs4 import BeautifulSoup

product_name = []
price = []
Description = []
reviews = []

title = input("enter your product = ").replace(" ","+")

for i in range(2,6):
    url = f"https://www.flipkart.com/search?q={title}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_ ="_4rR01T")
    for i in names:
        name = i.text
        product_name.append(name)

    prices = box.find_all("div",class_ ="_30jeq3 _1_WHN1")
    for i in prices:
        name=i.text.replace("₹","").replace(",","")
        price.append(name)
    
    description = box.find_all("ul",class_ ="_1xgFaf")
    for i in description:
        name=i.text
        Description.append(name)

    Reviews = box.find_all("div",class_ = "_3LWZlK")
    for i in Reviews :
        name =i.text
        reviews.append(name)
        
df =pd.DataFrame({"Product Names": product_name,"Prices": price, "Descriptions": Description})
print(len(product_name),len(price), len(description), len(reviews) )
df.to_csv(f"{title}.csv")
print("done")