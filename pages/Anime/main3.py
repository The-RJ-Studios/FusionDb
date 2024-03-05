#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

# import urllib3
# import requests
from js import document, console

random = [{
            "id":"6702",
            "title":"Fairy Tail",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx6702-4cW6E5AqQqqB.png"
        },{
            "id":"21355",
            "title":"Re:ZERO -Starting Life in Another World",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21355-IHaS50pvLYd0.jpg"
        },{
            "id":"11757",
            "title":"Sword Art Online",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx11757-Q9P2zjCPICq5.jpg"
        },{
            "id":"20605",
            "title":"Tokyo Ghoul",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx20605-fmnHdfurM7m6.jpg"
        },{
            "id":"21087",
            "title":"One Punch Man",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"20",
            "title":"NARUTO",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx20-YJvLbgJQPCoI.jpg"
        },{
            "id":"1",
            "title":"Cowboy Bebop",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1-CXtrrkMpJ8Zq.png"
        },{
            "id":"43",
            "title":"GHOST IN THE SHELL: Koukaku Kidoutai",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx43-LMGXobx4D6in.png"
        },{
            "id":"1535",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1535-lawCwhzhi96X.jpg"
        },{
            "id":"21459",
            "title":"My Hero Academia",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21459-DUKLgasrgeNO.jpg"
        }]
try:
# Fetching data
    rawData = random
    # Experimenting with creating a card div
    for data in rawData:
        console.log('Creating item', i)
        outerOuterDiv = document.getElementById('random')
        
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