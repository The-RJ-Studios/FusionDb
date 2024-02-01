from bs4 import BeautifulSoup
import requests
import js
import certifi
import urllib3
from js import console, document

# http = urllib3.PoolManager(
#     cert_reqs="https://acme-v02.api.letsencrypt.org/",
#     ca_certs=certifi.where()
# )
urllib3.disable_warnings()
# head="hello"
# document.getElementById("heading").innerHTML = head
r = requests.get('https://anilist.co/anime/918/Gintama/', verify=False)
console.log("Request sent")
soup = BeautifulSoup(r.content, 'html.parser')
console.log("Parsing content")
pcontent = soup.find_all('div',class_='content') #Finding The content 
console.log(pcontent)
# print('Finding content')
head = soup.find('h1').get_text()#finding h1 tag that contains heading and parsing it with get_text() funtion
console.log(head)
# document.getElementById("heading").innerHTML = head
# print(head) # Printing just the head
# body = soup.find('p',class_='description').get_text()
# print(body) #Printing just the body
# coverImgNP= soup.find('img',class_='cover')# Finding img 
# coverImg= coverImgNP['src'] #Finding src property from the tag
# print(coverImg)
# bannerNP= soup.find('div',class_='banner')
# banner= bannerNP['style']
# print(banner)
