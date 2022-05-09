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

def tweet ():

    while True : 

        response = requests.get(url)

        if response.ok :
            h = datetime.datetime.now().strftime('%H,%M,%S')

            if h == "07,00,00" or h == "18,00,00":

                soup = BeautifulSoup(response.text, 'lxml')
                info = soup.find('p')

                print(info.text)

                api.update_status("Info inutile : "+ info.text +"#infoinutile")
                time.sleep(1)
        else:
            print("error + tg ca remarche au prochain tweet")
            tweet()

tweet()
