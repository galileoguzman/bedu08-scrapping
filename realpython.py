from bs4 import BeautifulSoup
import requests

URL = "https://realpython.com/tutorials/django/"

response = requests.get(URL)
response_content = response.content

soup = BeautifulSoup(response_content, features="html.parser")

images = soup.find_all("img", class_="card-img-top")
for img in images:
    print(img["src"])
