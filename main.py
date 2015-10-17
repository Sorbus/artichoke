#!/usr/bin/python

#-----------------------------------------------------------------------
# artichoke:
#  - A small program which gathers basic information about twitter user habits.
#  - https://github.com/Sorbus/artichoke
#-----------------------------------------------------------------------

import config
import multiprocessing
import sys
import argparse
import shutil
from queue import Queue
from time import sleep
from worker import worker
from helpers import *
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('-n', '--number', help='number of tweets to fetch (default: 100, max: 3200)', type=check_range, default=100)
  parser.add_argument('-u', '--username', help='user to gather information about')
  parser.add_argument('-f', '--friends', help='gather information about accounts the user is following', action='store_true')
  parser.add_argument('-r', '--no-retweets', dest='retweets', help='do not include retweets in statistics', action='store_false')
  parser.set_defaults(retweets=True)
  parser.add_argument('-t', '--no-time', dest='time',help='omit information about hourly activity',action='store_false')
  parser.set_defaults(time=True)
  parser.add_argument('-v', '--vertical', help='display a vertical bar chart instead of a horizontal bar chart', action='store_true')
  parser.add_argument('-C', '--concise', help='only print results (note: no prompt for username will appear)', action='store_true')
  parser.add_argument('-w', '--width', help='width of bar chart to print (default: 80)', type=check_positive, default=shutil.get_terminal_size((80, 20)).columns)

  args = parser.parse_args()
  
  if not args.username:
    if not args.concise:
      print('User to query: ', end='')
    user = input()
  else:
    user = args.username

  queue = multiprocessing.Queue()
  signal = multiprocessing.Event()
                    
  p = multiprocessing.Process(target=worker, args=(signal,user,queue,args,))
  p.start()
    
  if not args.concise:
    print()
    message = 'Thinking ...'
    pointer = 0
    while not signal.is_set():
      if pointer < 11:
        print(message[pointer],end='')
        pointer += 1
      else:
        print('.',end='')
      sys.stdout.flush()
      sleep(0.05)
    print(' done!')
    print()
  else:
    signal.wait()
  
  while not queue.empty():
    print(queue.get(True))
    sleep(0.04)
