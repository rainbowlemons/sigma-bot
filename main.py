#!/usr/bin/python
import tweepy
import logging
import time

word_text = ("words_shuffled.txt", "r")
word_list = word_text.readlines()
word_index = 0

logger = logging.getLogger("sigmabot")
logger.setLevel(logging.INFO)

#Twitter Authentication
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

#Creating an api object
api = tweepy.API(auth)

try:
    api_verify_credentials()
    logger.info("Authentication OK")
except:
    logger.error("Error during authentication!")

def get_next_word():
    global word_list
    global word_index
    sigma = word_list[word_index]
    word_index += 1
    return sigma

def post_tweet(sigma):
    tweet = sigma + " is sigma."
    api.update_status(tweet)
    logger.info("Posted tweet: " + tweet)

if __name__ == "__main__":
    while True:
        sigma = get_next_word()
        post_tweet(sigma)
        time.sleep(60*60)
