import requests
from bs4 import BeautifulSoup
import json

 
url = 'https://steamdb.info/'

 
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

game_containers = soup.find_all("a", class_= "table-title")

for container in game_containers:
    title = container.span.text
 
    
    print(f"{title} ")
 
    
    
 