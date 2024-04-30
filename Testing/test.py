import requests
from bs4 import BeautifulSoup 
import pandas as pd

TARGET_URL = "https://www.geeksforgeeks.org/"
req = requests.get(TARGET_URL)
soup = BeautifulSoup(req.content , "html.parser")
text = soup.get_text()
text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
count = len(text.split())


data = {
    'target link' : [TARGET_URL],
    'scraped data': [text],
    'count of words' : count 
}

df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)

new = pd.read_csv("output.csv")
data = new['count of words']

print(data)