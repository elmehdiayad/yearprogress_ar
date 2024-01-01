import tweepy
import os
import datetime
import calendar
import math
import logging
import time
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')


client = tweepy.Client(bearer_token=bearer_token,
access_token=access_token,
access_token_secret=access_secret,
consumer_key=api_key,
consumer_secret=api_secret)


logging.basicConfig(filename='./logs.log', level=logging.DEBUG)


def get_percent():
    total_days = 0
    cursor = 1
    while cursor < datetime.datetime.now().month:
        total_days += calendar.monthrange(datetime.datetime.now().year, cursor)[1]
        cursor += 1
    total_days += datetime.datetime.now().day
    return math.floor(round(100 * total_days / 365, 1))


def generate_progress(percent):
    progress = []
    for i in range(20 - math.floor(percent / 5)):
        progress.append('░')
    for i in range(math.floor(percent / 5)):
        progress.append('▓')
    progress = ''.join(progress)
    return progress

def tweet_it():
    client.create_tweet(text=
        f'نحن الآن {get_percent()}% على مرور 2024\n {generate_progress(get_percent())}'
    )


if __name__ == '__main__':
    tweet_it()