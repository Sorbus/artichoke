# artichoke
A small program which gathers basic information about twitter user habits.

It's not as ominous as it sounds!

The main purpose of artichoke is to make it easy to see how many tweets users post per day, and when most of these tweets are posted.


## Planned features

* Add the ability to gather information about all accounts the user is following, and to present it in a consolidated form.
* Vertical bar graphs?
* Cute animations while waiting for results?

## Usage

artichoke is designed for python 3.4, and depends on [Python Twitter Tools](http://mike.verdone.ca/twitter/).

Run [authorize.py](https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-authorize.py), and follow its instructions to create and authorize the twitter application.

Run main.py [-n #]

### Sample output:

    User to query: twitter
    
    Thinking ....... done!
    
    Total tweets found: 100
    Average tweets per day: 1.852
    Median tweets per day: 2
    Peak tweets: 6 on Oct 06 2015
    Tweets by hour (+00 GMT):
    00: ||||
    01: |||
    02:
    03:
    04:
    05:
    06:
    07:
    08:
    09:
    10:
    11: |
    12:
    13: |||
    14: |||||
    15: |||||
    16: ||||||||||||
    17: ||||||||||||||
    18: |||||||||
    19: |||||||||||||
    20: ||||||||
    21: ||||||||||
    22: ||||||||
    23: |||||
