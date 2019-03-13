from twython import Twython, TwythonError
from config import *
import time
import schedule

last_rt = 0
tweet = 'I hope you know I pack a chainsaw! https://www.youtube.com/watch?v=ZpUYjpKg9KY'
# variables taken from config.py
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def quality_content():
    print('right now I\'m dangerous')
    twitter.update_status(status=tweet)


def retweet_durst():
    global last_rt
    data = Twython.get_user_timeline(screen_name='freddurst', count=1)
    if data['id'] != last_rt:
        last_rt = data['id']
        Twython.retweet(id=last_rt)


schedule.every().day.at('16:24').do(quality_content())
schedule.every().hour.do(retweet_durst())


try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except TwythonError as e:
    print('successfully broke stuff:\n')
    print(e)
