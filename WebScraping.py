#Will need to grab the request library
from bs4 import BeautifulSoup
import requests

#GET Request
req = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(req.text, "html.parser")


quote = soup.findAll("span", attrs={"class":"text"})
author = soup.findAll("small", attrs={"class":"author"})

#For Loop
for quote in quote:
    print(quote.text)
for author in author:
    print(author.text)

#Results
print(req)

print(req.content)