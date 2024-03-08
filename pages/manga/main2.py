# Json Comments
# "beautifulsoup4",
from js import document, console
latest = [{
            "id":"5163733",
            "title":"Netorare Manga no Kuzu Otoko ni Tensei Shita Hazu ga Heroine ga Yotte Kuru Ken",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx163733-DmPHIGCLQC62.png"
        },{
            "id":"115620",
            "title":"Erotical Wizard to 12-nin no Hanayome",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx115620-8hkYWhjEiUW5.jpg"
        },{
            "id":"169354",
            "title":"Two on Ice",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx169354-Uj6NebUoMcrU.jpg"
        },{
            "id":"171081",
            "title":"Shadow Eliminators",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/medium/b171081-UNik9vPHpMpu.png"
        },{
            "id":"163497",
            "title":"Nue no Onmyouji",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx163497-HNrC3KDTVxW5.jpg"
        },{
            "id":"169100",
            "title":"Mama Yuuyuu",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx169100-tQHWydcxdMVy.jpg"
        },{
            "id":"163495",
            "title":"Kill Ao",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx163495-tCWQW0kSvfjO.jpg"
        },{
            "id":"169355",
            "title":"Kagurabachi",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx169355-0MQ2NLOj1mL3.jpg"
        },{
            "id":"171004",
            "title":"Green Green Greens",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/medium/b171004-AhskbBVc3NXO.jpg"
        },{
            "id":"169904",
            "title":"Ogami Tsumiki to Kinichijou.",
            "image":"https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx30021-FE6kmrfpuKyb.jpg"
        }]
# Generating Request Headers
# console.clear()
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
        linknATag.href ="/info/index.html?type=manga&id="+ data['id']
        linknATag.innerHTML ="Read More"
except():
    console.log("Error occured")
# cardDiv = document.createElement('div')
# outerDiv.appendChild(cardDiv)

i=i+1