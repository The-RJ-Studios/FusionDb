#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

# import urllib3
# import requests
import json
from js import document, console
popular=[{
            "id":"16498",
            "title":"Shingeki no Kyojin",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx53390-1RsuABC34P9D.jpg"
        },{
            "id":"1535",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"5114",
            "title":"Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx5114-KJTQz9AIm6Wk.jpg"
        },{
            "id":"21087",
            "title":"One Punch Man",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21087-UV2tu6exrfXz.jpg"
        },{
            "id":"53390",
            "title":"Sword Art Online",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx11757-Q9P2zjCPICq5.jpg"
        },{
            "id":"21459",
            "title":"Boku no Hero Academia",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21459-DUKLgasrgeNO.jpg"
        },{
            "id":"101922",
            "title":"Kimetsu no Yaiba",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx101922-PEn1CTc93blC.jpg"
        },{
            "id":"20",
            "title":"Naruto",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx20-YJvLbgJQPCoI.jpg"
        },{
            "id":"11061",
            "title":"HUNTER×HUNTER (2011)",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx11061-sIpBprNRfzCe.png"
        },{
            "id":"20605",
            "title":"Tokyo Ghoul",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx20605-fmnHdfurM7m6.jpg"
        }]
# Generating Request Headers
# console.clear()

# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything

# <div class="card popu" id="0"> 
#            <img class="card-img" src="" alt="">
#           <div class="card-content">
#             <h2 class="card-title">Something awesome</h2>
#             <a href="/info/index.html" class="button">Read More</a>
#           </div>
#         </div>

i=1
# Loop for getting and displaying data inside the popular section
try:
# Fetching data
    rawData = popular
    # Experimenting with creating a card div
    for data in rawData:
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
        linknATag.href ="/info/index.html?type=anime&id="+ data['id']
        linknATag.innerHTML ="Read More"
except():
    console.log("Error occured")
# cardDiv = document.createElement('div')
# outerDiv.appendChild(cardDiv)

i=i+1
# print(item["title"])
# Loop for getting and displaying data inside the latest section    

# document.getElementById('cover').src=data['image']
# document.getElementById('title').innerHTML=data['title']
# document.getElementById('info').innerHTML = data['plot']
# document.getElementById('back-cover').src= data['images'][0]

# Printing head, body,coverImg, banner
