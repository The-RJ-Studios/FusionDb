# Json Comments
# "beautifulsoup4",
from js import document, console
random = [{
            "id":"53390",
            "title":"Shingeki no Kyojin",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx53390-1RsuABC34P9D.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        },{
            "id":"53390",
            "title":"DEATH NOTE",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        }]
# Generating Request Headers
# console.clear()
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