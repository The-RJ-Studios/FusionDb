#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

# import urllib3
# import requests
from js import document, console

# Generating Request Headers
# console.clear()
latest =[{
            "id":"154587",
            "title":"Sousou no Frieren",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx154587-n1fmjRv4JQUd.jpg"
        },{
            "id":"161645",
            "title":"Kusuriya no Hitorigoto",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx161645-7I8Cip7XRDhV.jpg"
        },{
            "id":"166216",
            "title":"Boku no Kokoro no Yabai Yatsu 2nd Season",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx166216-mK2CNMDLsBfW.jpg"
        },{
            "id":"155227",
            "title":"Kingdom 5th Season",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx155227-ZEAyBcZjSeet.jpg"
        },{
            "id":"21",
            "title":"ONE PIECE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx21-tXMN3Y20PIL9.jpg"
        },{
            "id":"151639",
            "title":"Ninja Kamui",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx151639-7KqJ7BgaM9Mx.png"
        },{
            "id":"151807",
            "title":"Solo Leveling",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx151807-m1gX3iwfIsLu.png"
        },{
            "id":"166794",
            "title":"Yubisaki to Renren",
            "image":"https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx166794-veSLL0zrrBhp.jpg"
        }]
# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything

try:
# Fetching data
    rawData = latest
    # Experimenting with creating a card div
    for data in rawData:
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
except():
    console.log("Error occured")
# cardDiv = document.createElement('div')
# outerDiv.appendChild(cardDiv)

i=i+1