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

    main.py [-h] [-n NUMBER] [-u USERNAME] [-f] [-r] [-t] [-v] [-C] [-w WIDTH]  
    
    optional arguments:  
    -h, --help            show this help message and exit  
    -n NUMBER, --number NUMBER  
                          number of tweets to fetch (default: 100, max: 3200)  
    -u USERNAME, --username USERNAME  
                          user to gather information about  
    -s, --self            gather information about yourself  
    -f, --friends         gather information about accounts the user is following  
    -r, --no-retweets     do not include retweets in statistics  
    -t, --no-time         omit information about hourly activity  
    -v, --vertical        display a vertical bar chart instead of a horizontal bar chart  
    -C, --concise         only print results
    -w WIDTH, --width WIDTH  
                          width of bar chart (default: width of terminal pr 80)  

### Sample output:

    > python .\main.py -n 300 -C -u twitter
    Total tweets found: 300
    Average tweets per day: 1.807
    Median tweets per day: 1
    Peak tweets: 10 on Mar 20 2015
    Tweet distribution by hour (+00 GMT):
    00: |||||||||||||||
    01: ||||||
    02: |
    03:
    04: |
    05: |
    06: ||
    07: |
    08:
    09:
    10:
    11: |
    12:
    13: |||||||
    14: |||||||||||
    15: ||||||||||
    16: |||||||||||||||||||||||||||||||||||||||||||||||||
    17: ||||||||||||||||||||||||||||||||||||||||||||||||||
    18: |||||||||||||||||||||||||||||
    19: |||||||||||||||||||||||||||||||||
    20: ||||||||||||||||||||
    21: ||||||||||||||||||||||||||||
    22: |||||||||||||||||||
    23: ||||||||||||||||
