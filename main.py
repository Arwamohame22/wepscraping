import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

Titles = []
Company_price = []
Links = []
result = requests.get("https://www.jobzella.com/search/egypt/jobs")
src = result.content
#print(src)
soup = BeautifulSoup(src, "lxml")
#print(soup)

Title = soup.find_all("h2",{"class":"card__info__title"})
company = soup.find_all("div",{"class":"card__info__item"})


for i in range(len(Title)):
    Titles.append(Title[i].text.strip())
    Links.append(Title[i].find("a").attrs['href'])
print(Titles)
print(Links)

for i in range(len(company)):
    Company_price.append(company[i].text.strip())
print(Company_price)

file_list = [Titles,Company_price,Links]
exp = zip_longest(*file_list)
with open("D:/omaar.csv","w") as file:
    wr = csv.writer(file)
    wr.writerow(["Job","Company & Place", "Links"])
    wr.writerows(exp)












