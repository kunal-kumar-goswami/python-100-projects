from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this formate YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0(windows NT 10.0; Win64; x64; rv:131.0) gecko/20100102 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100" + date 
response = requests.get(url = url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip()for song in song_name_spans]