# Json Comments
# "beautifulsoup4",
from js import document, console
popular =[
    {
            "id":"30002",
            "title":"Berserk",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30002-7EzO7o21jzeF.jpg"
        },{
            "id":"53390",
            "title":"Shingeki no Kyojin",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx53390-1RsuABC34P9D.jpg"
        },{
            "id":"30013",
            "title":"One Piece",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30013-tZVlfBCHbrNL.jpg"
        },{
            "id":"105778",
            "title":"Chainsaw Man",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx105778-82gwrvQV6OBc.png"
        },{
            "id":"63327",
            "title":"Tokyo Ghoul",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx63327-zvK2l9DjCqK4.jpg"
        },{
            "id":"105398",
            "title":"Solo Leveling",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx105398-b673Vt5ZSuz3.jpg"
        },{
            "id":"74347",
            "title":"One-Punch Man",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx74347-O6KMkECzHPOE.jpg"
        },{
            "id":"34632",
            "title":"Goodnight Punpun",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/nx34632-14deknANZitb.png"
        },{
            "id":"85486",
            "title":"My Hero Academia",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx85486-INqnYx8gL3eX.jpg"
        },{
            "id":"87216",
            "title":"Demon Slayer: Kimetsu no Yaiba",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx87216-c9bSNVD10UuD.png"
        }]
# Generating Request Headers
# console.clear()
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
        linknATag.href ="/info/index.html?type=manga&id="+ data['id']
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
