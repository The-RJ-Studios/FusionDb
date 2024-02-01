from datetime import datetime
import requests
import csv
import bs4

if __name__ == "__main__":
    print("Starting the script")
    with open('amazon_products_urls.csv', newlines='') as cs
    reader = csv.reader("amazon_products_urls.csv", delimiter=',')
    for row in reader:
        url =row[0]
        print(url)