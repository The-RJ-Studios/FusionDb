# Json Comments
# "beautifulsoup4",

import urllib3
# import json
import requests
from js import document, console, window

# Generating Request Headers
console.log("enter prompt")
query = document.getElementById('data1').innerHTML #Query string
movieUrl ='https://imdb-api.uzairshaikhking777.workers.dev/search?query='+ query
animeUrl ='https://manga-api-phi.vercel.app/meta/anilist/'+ query
mangaUrl='https://manga-api-phi.vercel.app/meta/anilist/'+ query
console.log(movieUrl,'\n', animeUrl, '\n', mangaUrl)
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}

# The above lines should be as it is No changes should be made
# def parser(data):
#     aData= list(data[0].key())
#     return aData # Currently not doing anything
def getData(url):
     res = requests.get(url, headers=req_header ,verify= False)
     return res.json()
# Printing Movie data
try:   
    urllib3.disable_warnings()
    movieData = getData(movieUrl)
    i=1
    results= movieData["results"]
    
    for item in results:
        # Experimenting with creating a card div
        console.log('Creating item', i)
        outerDiv = document.getElementById('result')
        cardDiv = document.createElement('div') #creating div element
        outerDiv.appendChild(cardDiv)#Important: append the elemt to the consecutive element before doing any changes to it!
        cardDiv.className="media-card" # adding class to it so style can be added 
        imageATag = document.createElement('a')# Importatnt the tag name should be in single quotes
        cardDiv.appendChild(imageATag)
        imageATag.className='cover'
        #----------------Same for this element----------------
        titleATag=document.createElement('a')
        cardDiv.appendChild(titleATag)
        titleATag.className = 'title'
        titleATag.innerHTML=item['title']
        imageATag.className="cover"
        #------------------------------------------------------
        imageTag = document.createElement('img')
        imageATag.appendChild(imageTag)
        imageTag.src = item['image']
        #-------------------------------------------------------
        linknATag = document.createElement('a')
        cardDiv.appendChild(linknATag)
        linknATag.className = 'button'
        linknATag.href ="/info/index.html?type=movie&id="+ item['id']
        linknATag.innerHTML ="Read More"
        i=i+1
        # print(item["title"])
    # console.log("Request sent")
    # document.getElementById('cover').src=data['image']
    # document.getElementById('title').innerHTML=data['title']
    # document.getElementById('info').innerHTML = data['plot']
    # document.getElementById('back-cover').src= data['images'][0]
    del results
except():
    window.alert('Error occurred. Please refresh the page or open console for more info.')
    console.log("Error encountered, please contacts the devs on Github repository. Open a pull request on: https://github.com/The-RJ-Studios/FusionDb ")
# Printing head, body,coverImg, banner

# Printing Anime data
try:
    animeData = getData(animeUrl)
    i=1
    results = animeData['results']
    for item in results:
        # Experimenting with creating a card div
        console.log('Creating item', i)
        outerDiv = document.getElementById('result')
        cardDiv = document.createElement('div') #creating div element
        outerDiv.appendChild(cardDiv)#Important: append the elemt to the consecutive element before doing any changes to it!
        cardDiv.className="media-card" # adding class to it so style can be added 
        imageATag = document.createElement('a')# Importatnt the tag name should be in single quotes
        cardDiv.appendChild(imageATag)
        imageATag.className='cover'
        #----------------Same for this element----------------
        titleATag=document.createElement('a')
        cardDiv.appendChild(titleATag)
        titleATag.className = 'title'
        titleATag.innerHTML=item['title']['userPreferred']
        imageATag.className="cover"
        #------------------------------------------------------
        imageTag = document.createElement('img')
        imageATag.appendChild(imageTag)
        imageTag.src = item['image']
        #-------------------------------------------------------
        linknATag = document.createElement('a')
        cardDiv.appendChild(linknATag)
        linknATag.className = 'button'
        linknATag.href ="/info/index.html?type=anime&id="+ item['id']
        linknATag.innerHTML ="Read More"
        i=i+1
        # print(item["title"])
    
     
    del results
except():
    window.alert('Error occurred. Please refresh the page or open console for more info.')
    console.log('Error encountered, please contacts the devs on Github repository. Open a pull request on: https://github.com/The-RJ-Studios/FusionDb ')
# Printing Manga Data
try:
    mangaData = getData(mangaUrl)
    i=1
    results = mangaData['results']
    for item in results:
        # Experimenting with creating a card div
        console.log('Creating item', i)
        outerDiv = document.getElementById('result')
        cardDiv = document.createElement('div') #creating div element
        outerDiv.appendChild(cardDiv)#Important: append the elemt to the consecutive element before doing any changes to it!
        cardDiv.className="media-card" # adding class to it so style can be added 
        imageATag = document.createElement('a')# Importatnt the tag name should be in single quotes
        cardDiv.appendChild(imageATag)
        imageATag.className='cover'
        #----------------Same for this element----------------
        titleATag=document.createElement('a')
        cardDiv.appendChild(titleATag)
        titleATag.className = 'title'
        titleATag.innerHTML=item['title']['userPreferred']
        imageATag.className="cover"
        #------------------------------------------------------
        imageTag = document.createElement('img')
        imageATag.appendChild(imageTag)
        imageTag.src = item['image']
        #-------------------------------------------------------
        linknATag = document.createElement('a')
        cardDiv.appendChild(linknATag)
        linknATag.className = 'button'
        linknATag.href ="/info/index.html?type=manga&id="+ item['id']
        linknATag.innerHTML ="Read More"
        i=i+1
        # print(item["title"])
    
    
    del results
except():
    window.alert('Error occurred. Please refresh the page or open console for more info.')
    console.log('Error encountered, please contacts the devs on Github repository. Open a pull request on: https://github.com/The-RJ-Studios/FusionDb ')