#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

import urllib3
import requests
from js import document, console

# Generating Request Headers
# console.clear()
baseUrl ='https://imdb-api.uzairshaikhking777.workers.dev/title/'
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
popular=['tt4978420','tt15398776','tt15239678','tt8521778','tt19864802','tt6263850','tt17351924','tt21064584','tt15009428']
# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything
def getData(inurl):
     res = requests.get(inurl, headers=req_header ,verify= False)
     return res.json()
try:   
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
    for item in popular:
        try:
            # Fetching data
            url=baseUrl+item
            data = getData(url)
            # Experimenting with creating a card div
            console.log('Creating item', i)
            outerOuterDiv = document.getElementById('popular')
            
            outerDiv = document.createElement('div')
            outerOuterDiv.appendChild(outerDiv)
            outerDiv.className = "card popu"
            
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
            h2tag.innerHTML = data['title']
            
            linknATag = document.createElement('a')
            contentCard.appendChild(linknATag)
            linknATag.className = 'button'
            linknATag.href ="/info/index.html?type=movie&id=" + data['id']
            linknATag.innerHTML ="Read More"
        except():
            continue
        # cardDiv = document.createElement('div')
        # outerDiv.appendChild(cardDiv)
        
        i=i+1
        # print(item["title"])
    # Loop for getting and displaying data inside the latest section    
    
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner
