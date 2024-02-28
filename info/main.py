# Importing needed things 
# from bs4 import BeautifulSoup
import sys
import urllib3
import json 
import requests
from js import document, console
# console.log(data1, data2)
query1 =  document.getElementById('Data1').innerHTML
query2 = document.getElementById('Data2').innerHTML
# Generating Request Headers
url ='https://imdb-api.uzairshaikhking777.workers.dev/title/'+query2
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}

# The above lines should be as it is No changes should be made
def parser(data):
    aData= list(data[0].key())
    return aData
def getData():
     res = requests.get(url, headers=req_header ,verify= False)
     return res.json()
try:
    
    urllib3.disable_warnings()
    data= getData()
    print(data['title'])
    # console.log("Request sent")
    document.getElementById('cover').src=data['image']
    document.getElementById('title').innerHTML=data['title']
    document.getElementById('info').innerHTML = data['plot']
    document.getElementById('back-cover').src= data['images'][0]
    
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner
console.log("For more info visit FusionDb on Github!")

