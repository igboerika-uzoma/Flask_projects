from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/asus-geforce-rtx-3080-ti-rog-strix-rtx3080ti-o12g-gaming/p/N82E16814126508"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)