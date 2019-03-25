from twython import Twython, TwythonError
from config import *
import time
import schedule

last_rt = 0
tweets = ['I hope you know I pack a chainsaw! https://www.youtube.com/watch?v=ZpUYjpKg9KY',
          'Some days you just don\'t wanna wake up https://www.youtube.com/watch?v=ZpUYjpKg9KY',
          'The only fighting game I play is Fight Club https://www.youtube.com/watch?v=ZpUYjpKg9KY',
          'I hope papa Fred notices me one day... https://www.youtube.com/watch?v=ZpUYjpKg9KY']
# variables taken from config.py
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def get_random():
    now = time.time()
    return int(now % 4)


def quality_content():
    print('right now I\'m dangerous')
    twitter.update_status(status=tweets[get_random()])


def retweet_durst():
    global last_rt
    data = twitter.get_user_timeline(screen_name='freddurst', count=1)
    if data['id'] != last_rt:
        last_rt = data[0]['id']
        twitter.retweet(id=last_rt)


schedule.every().day.at('16:24').do(quality_content)
schedule.every().hour.do(retweet_durst)


try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except TwythonError as e:
    print('successfully broke stuff:\n')
    print(e)
