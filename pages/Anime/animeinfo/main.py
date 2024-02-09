# from bs4 import BeautifulSoup
import json
import urllib3
import json 
import requests
from js import document, console

def parser(data):
    aData= list(data[0].key())
    return aData
try:   
    urllib3.disable_warnings()
    r = requests.get('https://imdb-api.uzairshaikhking777.workers.dev/title/tt2911666',verify= False)
    console.log("Request sent")
    print(r.json())
    # json = r()[0]
    
except():
    print("Error encountered")
# Printing head, body,coverImg, banner

