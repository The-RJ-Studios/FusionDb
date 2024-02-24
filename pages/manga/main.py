# Json Comments
# "beautifulsoup4",

import urllib3
# import json
import requests
from js import document, console

# Generating Request Headers
console.clear()
console.log("enter prompt")
query = "avengers" #Query string
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
    print("\n")
    # <div class="card card-1 popu" id="0"> 
    #            <img class="card-img" src="" alt="">
    #           <div class="card-content">
    #             <h2 class="card-title">Something awesome</h2>
    #             <a href="/pages/Anime/animeinfo/index.html" class="button">Read More</a>
    #           </div>
    #         </div>
    i=1
    results= data["results"]
    for item in results:
        # Experimenting with cresting a card div
        console.log('Creating item', i)
        outerDiv = document.getElementById('result')
        cardDiv = document.createElement('div')
        outerDiv.appendChild(cardDiv)
        cardDiv.className="media-card"
        imageATag = document.createElement('a')
        cardDiv.appendChild(imageATag)
        imageATag.className='cover'
        titleATag=document.createElement('a')
        cardDiv.appendChild(titleATag)
        titleATag.className = 'title'
        titleATag.innerHTML=item['title']
        imageATag.className="cover"
        imageTag = document.createElement('img')
        imageATag.appendChild(imageTag)
        imageTag.src = item['image']
        i=i+1
        # print(item["title"])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner
