from bs4 import BeautifulSoup
import requests
import os, os.path, csv

""" List of URLs for the extension names:
scrap_Video: http://dotwhat.net/type/video-movie-files
scrap_Audio: http://dotwhat.net/type/audio-music-files
scrap_Images: http://dotwhat.net/type/image-picture-files
scrap_Compressed: http://dotwhat.net/type/compressed-files
"""
# TODO: Can be made as a dictionary
scrap_Video = "http://dotwhat.net/type/video-movie-files"
scrap_Audio = "http://dotwhat.net/type/audio-music-files"
scrap_Images = "http://dotwhat.net/type/image-picture-files"
scrap_Compressed = "http://dotwhat.net/type/compressed-files"



listingurl = "http://localhost/test.html"  # scrap_Video
response = requests.get(listingurl)
soup = BeautifulSoup(response.text, "html.parser")

listings = []
elementsList = soup.find_all("input")

# Sample of the input line:
# <input class="iExt" type="hidden" value="ASWCS"/>
print("Getting elements...")
for elements in elementsList:
    listings.append(elements.get('value'))
for i in listings:
    with open(r"result.txt", 'a',) as txtfile:
        txtfile.write(i + '\n')

# with open("result.csv", 'w', newline='', encoding='utf-8') as toWrite:
#     writer = csv.writer(toWrite, delimiter=',')
#     writer.writerows(listings)
#     print("Listings fetched.")
