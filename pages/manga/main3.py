# Json Comments
# "beautifulsoup4",

import urllib3
# import json
import requests
from js import document, console
random = ['116778','75989','122397','113138','30012','106130','30007','140475','108556','86508']
# Generating Request Headers
# console.clear()
providerQuery = '?provider=mangadex'
baseurl ='https://manga-api-phi.vercel.app/meta/anilist-manga/info/'
print(baseurl)
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
def getData(inurl):
    res = requests.get(inurl, headers=req_header ,verify= False)
    return res.json()
# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything

urllib3.disable_warnings()

# <div class="card popu" id="0"> 
#            <img class="card-img" src="" alt="">
#           <div class="card-content">
#             <h2 class="card-title">Something awesome</h2>
#             <a href="/info/index.html" class="button">Read More</a>
#           </div>
#         </div>

i=1

# Loop for getting and displaying data inside the popular section
for item in random:
    try:
        url=baseurl+item+providerQuery
        data = getData(url)
        console.log('Creating item', i)
        outerOuterDiv = document.getElementById('random')
        
        outerDiv = document.createElement('div')
        outerOuterDiv.appendChild(outerDiv)
        outerDiv.className = "card popi"
        
        imageTag = document.createElement('img')
        outerDiv.appendChild(imageTag)
        imageTag.className="card-img"
        imageTag.src= data['image']
        
        contentCard = document.createElement('div')
        outerDiv.appendChild(contentCard)
        contentCard.className = "card-content"
        
        h2tag = document.createElement('h2')
        contentCard.appendChild(h2tag)
        h2tag.className ="card-title"
        h2tag.innerHTML = data['title']['romaji']
        
        linknATag = document.createElement('a')
        contentCard.appendChild(linknATag)
        linknATag.className = 'button'
        linknATag.href ="/info/index.html?type=manga&id="+ data['id']
        linknATag.innerHTML ="Read More"
    except():
        continue
        
    
    i=i+1