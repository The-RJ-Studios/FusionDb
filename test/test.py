import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = "https://remoteok.com/api"
USER_AGENT= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
REQUEST_HEADER = {
    'User-Aget': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}
def get_job_posting():
    res = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
    print("Request Send")
    return res.json()
def output_job_xls(data):
    wb = Workbook()
    job_sheet =wb.add_sheet('Jobs')
    headers=list(data[0].keys())
    

if  __name__=="__main__":
    print("Dependencies installed successfully.")
    json= get_job_posting()[1:]
    # print(json)
    print('Response received successfully')
    output_job_xls(json)
