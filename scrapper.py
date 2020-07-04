from bs4 import BeautifulSoup
import requests

URL = "https://realpython.com/"

response = requests.get(URL)
response_content = response.content

soup = BeautifulSoup(response_content, features="html.parser")

topics = soup.find_all("a", class_="badge badge-light text-muted")

topics_list = []
for anchor in topics:
    topics_list.append(anchor.text)

topics_list = list(dict.fromkeys(topics_list))

responses_html_topics = []
for item in topics_list:
    topic_url = f"{URL}tutorials/{item}/"
    response_topic = requests.get(topic_url)
    if response_topic.status_code == 200:
        responses_html_topics.append(response_topic.content)
    print(f"Process for {topic_url}")

# ------------
# print the title of each sitio

for site in responses_html_topics:
    site_soup = BeautifulSoup(site, features="html.parser")
    print(site_soup.title)
