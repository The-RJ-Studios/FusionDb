#For Detailed breakdown of tags open search/main.py
# Json Comments
# "beautifulsoup4",

import urllib3
import requests
from js import document, console

# Generating Request Headers
# console.clear()
url ='https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5',
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzM5MTA5ZGMyODY2NDk5NjRjYTE1MGVmOWI5YTkyNyIsInN1YiI6IjY2MGJkZDA0YzhhNWFjMDE2Mzc4NTMzMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BIPcYHWiu1lzESx2MqI7Gm4HWduajybMQZJe1fQWcZg"

}

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

    try:
        # Fetching data
        urllib3.disable_warnings()
        data = getData(url)
        rawData = data['results']
        # Experimenting with creating a card div
        for data in rawData:
            if (i!=11):
                console.log('Creating item', i)
                outerOuterDiv = document.getElementById('popular')
                
                outerDiv = document.createElement('div')
                outerOuterDiv.appendChild(outerDiv)
                outerDiv.className = "card popu"
                
                imageTag = document.createElement('img')
                outerDiv.appendChild(imageTag)
                imageTag.className="card-img"
                imageTag.src= 'https://image.tmdb.org/t/p/original'+ data['poster_path']
                
                contentCard = document.createElement('div')
                outerDiv.appendChild(contentCard)
                contentCard.className = "card-content"
                
                h2tag = document.createElement('h2')
                contentCard.appendChild(h2tag)
                h2tag.className ="card-title"
                h2tag.innerHTML = data['original_title']
                
                linknATag = document.createElement('a')
                contentCard.appendChild(linknATag)
                linknATag.className = 'button'
                linknATag.href ="/info/index.html?type=anime&id="+ str(data['id'])
                linknATag.innerHTML ="Read More"
                i+=1
            else:
                break 
        
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

except():
    print("Error encountered")
# Printing head, body,coverImg, banner
