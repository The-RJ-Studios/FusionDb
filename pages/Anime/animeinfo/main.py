# from bs4 import BeautifulSoup
import urllib3
import json 
import requests
from js import document, console
try:   
    urllib3.disable_warnings()
    r = requests.get('https://imdb-api.uzairshaikhking777.workers.dev/title/tt2911666',verify= False)
    console.log("Request sent")
    p = json5.decode(r.read())
    console.log(p)
    parseR= json.loads(r)
    console.log(parseR, "help")
    
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner

