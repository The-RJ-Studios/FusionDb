#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

import urllib3
import requests
from js import document, console

# Generating Request Headers
# console.clear()

# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything
url = 'https://fusiondb.pages.dev/pages/Anime/list.json'
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
def getData(inurl):
     res = requests.get(inurl, headers=req_header ,verify= False)
     return res.json()
i=1
try:
# Fetching data
    urllib3.disable_warnings()
    data = getData(url)
    rawData = data['latest']['results']
    
    # Experimenting with creating a card div
    for data in rawData:
        if (i!=10):
            console.log('Creating item', i)
            outerOuterDiv = document.getElementById('latest')
            
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
            linknATag.href ="/info/index.html?type=anime&id="+ data['id']
            linknATag.innerHTML ="Read More"
            i=i+1
        else:
            break
except():
    console.log("Error occured")
    # cardDiv = document.createElement('div')
    # outerDiv.appendChild(cardDiv)
