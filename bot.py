import tweepy
import requests
from bs4 import BeautifulSoup
import time
import datetime

# Authenticate to Twitter
auth = tweepy.OAuthHandler("key", "key_secret")
auth.set_access_token("token", "token_secret")

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
