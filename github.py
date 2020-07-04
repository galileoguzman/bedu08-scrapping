import csv
import json
import requests

URL = "https://api.github.com/"

response = requests.get(URL)
response_text = response.text
response_json = json.loads(response_text)

csv_columns = response_json.keys()
csv_row = response_json.items()

with open ('github.csv'. 'w') as csv_file:
    # Write dict
    write = csv.DictWriter(csv_file, fieldnames=csv_columns)
