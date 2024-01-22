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
if  __name__=="__main__":
    print("Dependencies installed successfully.")
def get_job_posting():
    re = requests.get(url=BASE_URL)
    print("Request Send")