#-----------------------------------------------------------------------
# worker module for artichoke:
#  - This is where most of the core logic is!
#  - This file won't work very well if you run it by itself, though ...
#  - https://github.com/Sorbus/artichoke
#-----------------------------------------------------------------------

import config
from twitter import *
from datetime import datetime
from datetime import timedelta
from twitter import *

def worker(signal, user, queue, args):
  twitter = Twitter(
      auth = OAuth( config.access_key,
                    config.access_secret,
                    config.consumer_key,
                    config.consumer_secret))

  results = twitter.statuses.user_timeline(screen_name = user, count = args.number)

  date = {}
  hour = {}

  start = results[len(results)-1]['created_at']
  start = datetime.strptime(start, '%a %b %d %H:%M:%S +0000 %Y')

  while start.day <= datetime.now().day:
    date[datetime.strftime(start, '%a %b %Y')] = 0
    start += timedelta(days=1)

  for x in range(00,24):
    hour[str(x).zfill(2)] = 0

  for status in results:
    try:
      date[status['created_at'][4:10] + status['created_at'][-5:]] += 1
    except KeyError:
      date[status['created_at'][4:10] + status['created_at'][-5:]] = 1
    
    try:
      hour[status['created_at'][11:13]] += 1
    except KeyError:
      hour[status['created_at'][11:13]] = 1
      
  peak = list(date.keys())[0]
  med = []
      
  for each in date.keys():
    if date[peak] < date[each]:
      peak = each
    med.append(date[each])
      
  med = sorted(med)[int(len(med)/2)]
  
  queue.put('Total tweets found: ' + str(len(results)))
  queue.put('Average tweets per day: ' + str(round(len(results)/len(date),3)))
  queue.put('Median tweets per day: ' + str(med))
  queue.put('Peak tweets: ' + str(date[peak]) + ' on ' + peak)

  queue.put('Tweets by hour (+00 GMT):')  
  for each in sorted(hour.keys()):
    queue.put(each + ': ' + '|'*hour[each])
  signal.set()
  return