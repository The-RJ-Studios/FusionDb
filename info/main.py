# Just For testing parameters:
# Movie : ?type=movie&id=tt0372784
# Manga : ?type=manga&id=30013
# Anime : ?type=anime&id=113415
# Importing needed things 
# from bs4 import BeautifulSoup
import sys
import urllib3
import json 
import requests
from js import document, console, window

# Generating Request Headers
userAgent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
req_header= {
    'User-Agent' : userAgent,
    'Accept-Language': 'en-US, en;q=0.5'
}
queryType =  document.getElementById('Data1').innerHTML
queryId = document.getElementById('Data2').innerHTML

def parser(data):
    aData= list(data[0].key())
    return aData
def getData(inUrl):
    res = requests.get(inUrl, headers=req_header ,verify= False)
    return res.json()
# The above lines should be as it is No changes should be made

# Data insertion

# Movie data insertion
if queryType=='movie':
    url ='https://imdb-api.uzairshaikhking777.workers.dev/title/'+queryId

    try:
        
        urllib3.disable_warnings()
        data= getData(url)
        console.log(data['title'])
        # console.log("Request sent")
        document.getElementById('cover').src = data['image']
        document.getElementById('title').innerHTML = data['title']
        document.getElementById('info').innerHTML = data['plot']
        document.getElementById('back-cover').src = data['images'][0]
        document.getElementById('type').innerHTML = data['contentType']
        document.getElementById('con-rating').innerHTML = data['contentRating']
        document.getElementById('video').src ='https://www.youtube.com/embed/ttUlSmEkS9g?si=QzM0HO6WurLBI7wX'
        document.getElementById('status').innerHTML = data['productionStatus']
        release =  str(data['releaseDetailed']['day'])+"/ "+str(data['releaseDetailed']['month']) + "/ " + str(data['releaseDetailed']['year'])
        
        document.getElementById('release').innerHTML = release
        document.getElementById('duration').innerHTML =data['runtime']
        document.getElementById('rating').innerHTML =str(data['rating']['star'])
        
        genre =""
        for ele in data['genre']:
            if genre == "":
                genre = ele
            else:
                genre = genre + ",\n " + ele
        document.getElementById('genre').innerHTML = genre
    except():
        console.log("Error encountered while retriving movie data. please reload the page or open issue on github")
        window.alert("Please check your internet connection and refresh the page")
# Manga data insertion
elif queryType == 'manga':
    url ='https://manga-api-phi.vercel.app/meta/anilist-manga/info/'+queryId +'?provider=mangadex'
    
    try:
        urllib3.disable_warnings()
        data= getData(url)
        # Cover
        document.getElementById('cover').src = data['image']
        # Title
        if data['title']['english']== None:
            document.getElementById('title').innerHTML = data['title']['romaji']
        else:
            document.getElementById('title').innerHTML = data['title']['english']
        document.getElementById('info').innerHTML = data['description'] # Description/ Info
        document.getElementById('back-cover').src = data['cover']
        document.getElementById('type').innerHTML = data['type'] # Type
        document.getElementById('con-rating').innerHTML = str(data['rating']) + "th" # Ratings
        document.getElementById('video').src = 'https://www.youtube.com/embed/'+ data['trailer']['id']+'?si=QzM0HO6WurLBI7wX' # Video Insertion 
        document.getElementById('status').innerHTML = data['status'] # Status
        
        # Release
        release = data['releaseDate'] 
        document.getElementById('release').innerHTML = release
        
        document.getElementById('duration-tag').style.display ='none' # Duration
        document.getElementById('rating').innerHTML = str(data['rating']) #Rating
        # Genre insertion
        genre=""
        for ele in data['genres']:
            if genre == "":
                genre = ele
            else:
                genre = genre + ",\n " + ele 
        document.getElementById('genre').innerHTML = genre
    except():
        console.log("Error encountered while retriving movie data. please reload the page or open issue on github")
        window.alert("Please check your internet connection and refresh the page")
# Anime Data insertion
elif queryType == 'anime':
    pass
    url ='https://manga-api-phi.vercel.app/meta/anilist/info/'+queryId
    try:
        urllib3.disable_warnings()
        data= getData(url)
        document.getElementById('cover').src = data['image']
        if data['title']['english']== None:
            document.getElementById('title').innerHTML = data['title']['romaji']
        else:
            document.getElementById('title').innerHTML = data['title']['english']
        document.getElementById('info').innerHTML = data['description']
        document.getElementById('back-cover').src = data['cover']
        document.getElementById('type').innerHTML = data['type']
        document.getElementById('con-rating').innerHTML = str(data['rating']) + "th"
        document.getElementById('video').src = 'https://www.youtube.com/embed/'+ data['trailer']['id']+'?si=QzM0HO6WurLBI7wX'
        genre =""
        for ele in data['genres']:
            if genre == "":
                genre = ele
            else:
                genre = genre + ",\n " + ele 
        document.getElementById('genre').innerHTML = genre
        document.getElementById('status').innerHTML = data['status'] # Status
        
        # Release
        release = data['releaseDate'] 
        document.getElementById('release').innerHTML = release
        
        document.getElementById('duration-tag').style.display ='none' # Duration
        document.getElementById('rating').innerHTML = str(data['rating']) 
    except():
        console.log("Error encountered while retriving movie data. please reload the page or open issue on github")
        window.alert("Please check your internet connection and refresh the page")
        

# Printing head, body,coverImg, banner
console.log("For more info visit FusionDb on Github!")

