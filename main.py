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
from queue import Queue
from time import sleep
from worker import worker

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('-n', '--number', help='number of tweets to fetch (default: 100)', type=int, default=100)
  parser.add_argument('-u', '--username', help='user to gather information about')

  args = parser.parse_args()

  if not args.username:
    print('User to query: ', end='')
    user = input()
  else:
    user = args.username

  queue = multiprocessing.Queue()
  signal = multiprocessing.Event()
                    
  p = multiprocessing.Process(target=worker, args=(signal,user,queue,args,))
  p.start()
    
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
  
  while not queue.empty():
    print(queue.get(True))
    sleep(0.04)
    
