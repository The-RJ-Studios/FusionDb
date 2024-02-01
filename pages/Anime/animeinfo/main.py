from bs4 import BeautifulSoup
import requests
import js
import ssl
from js import document, console
# # from pyscript import Element
# def extract_data_from_page(filename):
#     s = BeautifulSoup(open(filename), "html.parser")
head ='Loaded'
try:
    
    print("Sending request")
    r = requests.get('https://anilist.co/anime/918/Gintama/')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print("Parsing the content")
    # head = soup.find('h1').get_text() #finding h1 tag that contains heading and parsing it with get_text() funtion
    # body = soup.find('p',class_='description').get_text()
    # coverImgNP= soup.find('img',class_='cover')# Finding img 
    # coverImg= coverImgNP['src'] #Finding src property from the tag
    # bannerNP= soup.find('div',class_='banner')
    # banner= bannerNP['style']
    # print("Placing parsed content in the place")
    document.getElementById("title").innerHTML = head
    # console.log("Hello")
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner

