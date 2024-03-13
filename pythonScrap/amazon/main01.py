import requests 
from bs4 import BeautifulSoup
from time import sleep

header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Accept-Language':'en-US,en;q=0.5'})
keywords = ["smart watch for men","smart watch","noise smart watches","smart watch for women","noise"]


for i in range(3):
    for keyword in keywords:
        try:
            url = f"https://www.amazon.in/s?k={keyword.replace(" ", "+")}&page=2&crid=T29UP548C8TS&qid=1710230873&sprefix=smart+%2Caps%2C229&ref=sr_pg_2"
            r = requests.get(url,headers=header)
            print(r)r
            soup = BeautifulSoup(r.text, "html.parser")

            titles = soup.findAll("span", class_ ="a-size-medium a-color-base a-text-normal")
            prices = soup.findAll("span", class_ = "a-price-whole")
            reviews = soup.findAll("span", class_="a-size-base s-underline-text")
            deals = soup.findAll("span", class_="a-badge-text")

            lst = [len(titles), len(prices),len(reviews),len(deals)]

            file = open(f"{keyword}.csv","a")
            for i in range(min(lst)):
                file.write(f"{titles[i].text.replace(",", "_")}, {prices[i].text.replace(",", "_")},{reviews[i].text.replace(",", "_")},{deals[i].text.replace(",", "_")}\n")
            file.close()
        except:
            print(f"Internet issue for {keyword}")
        sleep(12 * 60)




