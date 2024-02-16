# Importing needed things 
# from bs4 import BeautifulSoup
import urllib3
# import json
import requests
# from js import document, console

# Generating Request Headers
query = input("Enter query : ") #Query string
url ='https://imdb-api.uzairshaikhking777.workers.dev/search?query='+ query
print(url)
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything
def getData():
     res = requests.get(url, headers=req_header ,verify= False)
     return res.json()
try:   
    urllib3.disable_warnings()
    data= getData()
    # print(data)
    print("\n")
    results= data["results"]
    for item in results:
        print("""<div class="media-card">
           <a href="" class="cover">

          <img src="/pics/Ghoul.jpg" alt="" class="image loaded">

           </a> 
           <a href="" class="title">

           Title of an anime long title

           </a>
          </div>""")
        print(item["title"])
    # print(data['title'])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner
