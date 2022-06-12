import json, config, re, os
from requests_oauthlib import OAuth1Session

API_KEY = config.TWITTER_API['API_KEY']
API_KEY_SECRET = config.TWITTER_API['API_KEY_SECRET']
ACCESS_TOKEN = config.TWITTER_API['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config.TWITTER_API['ACCESS_TOKEN_SECRET']

CODES_DIR = './codes/'
LOG_PATH = 'log.md'

def createContent():
    f = open(LOG_PATH, 'r')
    log = f.read()
    f.close()

    day_num = sum(os.path.isdir(CODES_DIR) for tmp in os.listdir(CODES_DIR))
    log_today = re.search(f'Day {day_num}:' + r'(.*)', log, flags=re.DOTALL).group(0)
    progress = re.search("Today's Progress\*\*: " + r'(.*)', log_today).group(1)
    thoughts= re.search("Thoughts\*\*: " + r'(.*)', log_today).group(1)
    tags = "@gdsciter #100DaysOfCode #gdsciter #developerstudentclubs #googledeveloperstudentclubs"

    tweet_content = f'Day{day_num}\n\n{progress}\n{thoughts}\n\n{tags}'

    return tweet_content

twitter = OAuth1Session(
    API_KEY,
    client_secret=API_KEY_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_TOKEN_SECRET
)

payload = {"text": createContent()}
res = twitter.post("https://api.twitter.com/2/tweets", json=payload)

if res.status_code == 201:
    print("Successfully posted")
else:
    print("Failed to post : %d"% res.status_code)