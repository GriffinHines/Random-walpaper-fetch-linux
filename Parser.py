import requests
from bs4 import BeautifulSoup
import re

URL = "https://wall.alphacoders.com/random.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

pictureLines = soup.find_all("div", class_="boxgrid")

line = str(pictureLines[0])

wallpaperId = line.split("=")
wallpaperId = wallpaperId[3].split('"')
wallpaperId = wallpaperId[0]

#print(wallpaperId)

#imageLink = "https://wall.alphacoders.com/wallpaper.php?i=" + wallpaperId + "&w=1920&h=1080&type=stretch"
URL = "https://wall.alphacoders.com/big.php?i=" + wallpaperId
#print(URL)

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

soup = str(soup)

downloadLink = str(re.split("picture", soup)[0])
downloadLink = str(re.split("href", downloadLink)[-1])
downloadLink = downloadLink.split('"')
print(downloadLink[1], end=" ")
