import tweepy
import requests
from bs4 import BeautifulSoup
import time
import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler("QyQcJ84xiv2obPRb7Isrhuqrx", "3wZI2fkZFJuJq372t4MN3eirckLv1u0ButuyBrQXTGY5Sy0RGF")
auth.set_access_token("1519341833347866624-AChZr1S7pGfVTD4Hb7q2vK5n2tbjDe", "w65AIKnRwrie8glS1ezVhV0ICSuyzVfPYuyaCsIJZ1yOd")

# Create API object
api = tweepy.API(auth)

url = 'https://m.savoir-inutile.com/'

while True : 

    response = requests.get(url)

    if response.ok :
        h = datetime.datetime.now().strftime('%H,%M,%S')

        if h == "08,00,00" or h == "19,00,00":

            soup = BeautifulSoup(response.text, 'lxml')
            info = soup.find('p')

            print(info.text)

            api.update_status("Info inutile du soir : "+ info.text +"#infoinutile")
            time.sleep(1)