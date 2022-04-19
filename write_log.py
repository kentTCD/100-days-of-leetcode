import os
from datetime import datetime, timedelta
import sys

CODES_DIR = './codes/'
LOG_PATH = 'log.md'
GIT_REPO_PATH = 'https://github.com/tsuchi-ken/100-days-of-leetcode/'

def createLinksToWork():
    added_files = sorted(os.listdir(CODES_DIR + 'Day' + str(day_num)))
    i = 1
    links_to_work = '**Link(s) to work**:'
    for file_name in added_files:
        name_split = file_name.split('-')
        name_split[0] = name_split[0] + '.'
        arrng_name = ' '.join(name_split).replace('.py', '')
        url = GIT_REPO_PATH + 'blob/master/codes/Day' + str(day_num) + '/' + file_name
        links_to_work = links_to_work + '\n' + str(i) + '. ' + '[' + arrng_name + ']' + '(' + url + ')'
        i = i + 1

    return links_to_work

argv = sys.argv
if len(argv) >= 2:
    yesterday_flag = True if argv[1] in ['true', 'True', 'TRUE'] else False
else:
    yesterday_flag = False

day_num = sum(os.path.isdir(CODES_DIR) for tmp in os.listdir(CODES_DIR))
today = datetime.now() if not yesterday_flag else datetime.now()- timedelta(1)

date = '### Day ' + str(day_num) + ': ' + today.strftime('%B') + ' ' + str(today.day) + ', ' + str(today.year)
todays_progress = "**Today's Progress**: "
thoughts = "**Thoughts**: "
links_to_work = createLinksToWork()

content = '\n' + date + '\n\n' + todays_progress + '\n\n' + thoughts + '\n\n' + links_to_work

with open(LOG_PATH, 'a') as f:
    print(content, file=f)

bar = ' ----------------- '
print(bar + "Added Log For: " + date[4:] + bar)
