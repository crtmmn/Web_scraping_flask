import requests
from bs4 import BeautifulSoup
import pandas as pd
 
url = "https://filman.cc/online"
response = requests.get(url)
 
soup = BeautifulSoup(response.content, "html.parser")
 
items = soup.find_all("div", {"class" : "col-xs-6 col-sm-2"})
 
# print(items)
 
results = []
 
for item in items:
    imageURL = item.find("img", {"class" : "img-responsive"})
    imageURL = imageURL.get("src")
    title = item.find("h1", {"class" : "film_title"}).text
    year = item.find("div",{"class" : "film_year"}).text
 
    result = {
        "imageURL" : imageURL,
        "title" : title,
        "year" : year
    }
 
    results.append(result)
 
df = pd.DataFrame(results)
 
df.to_csv("filman.csv", index = False)