# Json Comments
# "beautifulsoup4",
import threading
import urllib3
# import json
import requests
from js import document, console

# Generating Request Headers
query = "john wick" #Query string
url ='https://imdb-api.uzairshaikhking777.workers.dev/search?query='+ query
print(url)
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
console.log("Why the hell am i doing this?")
# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything
def getData():
     res = requests.get(url, headers=req_header ,verify= False)
     return res.json()
def getDiv1Data():
    try:
        urllib3.disable_warnings()
        data= getData()
        print("\n")
    # """<div class="media-card"> #cardDiv
    #        <a href="" class="cover">

    #       <img src="" alt="" class="image loaded">

    #        </a> 
    #        <a href="" class="title">

    #        Title of an anime long title

    #        </a>
    #       </div>"""
        results= data["results"]
        for item in results:
            # Experimenting with cresting a card div
            console.log(item["title"])
            outerDiv = document.getElementById('div1')
            cardDiv = document.createElement('div')
            outerDiv.appendChild(cardDiv)
            cardDiv.className="media-card"
            imageATag = document.createElement('a')
            cardDiv.appendChild(imageATag)
            titleATag=document.createElement('a')
            cardDiv.appendChild(titleATag)
            titleATag.innerHTML=item['title']
            # imageATag.className="cover"
            imageTag = document.createElement('img')
            imageATag.appendChild(imageTag)
            imageTag.src = item['image']
        
        # print(item["title"])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
    except():
        console.log("Error encountered")
def getDiv2Data():
    try:
        urllib3.disable_warnings()
        data= getData()
        print("\n")
    # """<div class="media-card"> #cardDiv
    #        <a href="" class="cover">

    #       <img src="" alt="" class="image loaded">

    #        </a> 
    #        <a href="" class="title">

    #        Title of an anime long title

    #        </a>
    #       </div>"""
        results= data["results"]
        for item in results:
            # Experimenting with cresting a card div
            console.log(item["title"])
            outerDiv = document.getElementById('div2')
            cardDiv = document.createElement('div')
            outerDiv.appendChild(cardDiv)
            cardDiv.className="media-card"
            imageATag = document.createElement('a')
            cardDiv.appendChild(imageATag)
            titleATag=document.createElement('a')
            cardDiv.appendChild(titleATag)
            titleATag.innerHTML=item['title']
            # imageATag.className="cover"
            imageTag = document.createElement('img')
            imageATag.appendChild(imageTag)
            imageTag.src = item['image']
        
        # print(item["title"])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
    except():
        console.log("Error encountered")
def getDiv3Data():
    try:
        urllib3.disable_warnings()
        data= getData()
        print("\n")
    # """<div class="media-card"> #cardDiv
    #        <a href="" class="cover">

    #       <img src="" alt="" class="image loaded">

    #        </a> 
    #        <a href="" class="title">

    #        Title of an anime long title

    #        </a>
    #       </div>"""
        results= data["results"]
        for item in results:
            # Experimenting with cresting a card div
            console.log(item["title"])
            outerDiv = document.getElementById('div3')
            cardDiv = document.createElement('div')
            outerDiv.appendChild(cardDiv)
            cardDiv.className="media-card"
            imageATag = document.createElement('a')
            cardDiv.appendChild(imageATag)
            titleATag=document.createElement('a')
            cardDiv.appendChild(titleATag)
            titleATag.innerHTML=item['title']
            # imageATag.className="cover"
            imageTag = document.createElement('img')
            imageATag.appendChild(imageTag)
            imageTag.src = item['image']
            console.log("Created Element")
        
        # print(item["title"])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
    except():
        console.log("Error encountered")

# Printing head, body,coverImg, banner
# t1=threading.Thread(target=getDiv1Data)
# t1.start()
console.log("calling the function withou the thread")
getDiv1Data()
# t2=threading.Thread(target=getDiv2Data)
# t3=threading.Thread(target=getDiv3Data)