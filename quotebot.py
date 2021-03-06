#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import ssl
import time

import tweepy
import wikiquote

ssl._create_default_https_context = ssl._create_unverified_context
CONSUMER_KEY = '12345...'
CONSUMER_SECRET = '12345...'
ACCESS_KEY = '12345...'
ACCESS_SECRET = '12345...'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def confronto(quotes):
    possibilities = []
    possibilities.extend([random.choice(wikiquote.quotes('The_Fellowship_of_the_Ring')),
                         random.choice(wikiquote.quotes('The_Two_Towers')),
                         random.choice(wikiquote.quotes('The_Return_of_the_King'))])
    quote = random.choice(possibilities)
    if quote not in quotes:
        if len(quote)<141 and quote is not None:
            quotes.append(quote)
            print(quote)
            with open('database.json', 'w') as data_file:
                json.dump(quotes, data_file)
            print('*************')
            print(quotes)
            print('*************')
        else:
            confronto(quotes)
    else:
        confronto(quotes)

def run():
    with open('database.json', 'r') as data_file:
        quotes = json.load(data_file)
    while True:
        confronto(quotes)
        time.sleep(10)

if __name__ == "__main__":
    run()