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
latest=['tt29467317','tt16156736','tt13103028','tt30644010','tt21621494','tt30488398','tt27524116','tt30495098','tt13483212','tt30146725']
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
    # Loop for getting and displaying data inside the latest section    
    for item in latest:
        try:
            # Fetching data
            url=baseUrl+item
            data = getData(url)
            # Experimenting with creating a card div
            console.log('Creating item', i)
            outerOuterDiv = document.getElementById('latest')
            
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
            h2tag.innerHTML = data['title']
            
            linknATag = document.createElement('a')
            contentCard.appendChild(linknATag)
            linknATag.className = 'button'
            linknATag.href ="/info/index.html?type=anime&id="+ data['id']
            linknATag.innerHTML ="Read More"
        except():
            continue    
        # cardDiv = document.createElement('div')
        # outerDiv.appendChild(cardDiv)
        
        i=i+1
        # print(item["title"])
except():
    print("Error encountered")