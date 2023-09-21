
from bs4 import BeautifulSoup
import requests

year = input("Which year would you like to travel to (YY-MM-DD format)? ")


response = requests.get("https://www.billboard.com/charts/hot-100/" + year)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)