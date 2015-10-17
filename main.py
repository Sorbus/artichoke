import config
from twitter import *

twitter = Twitter(
		auth = OAuth( config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

print('User to query: ', end='')
user = input()

results = twitter.statuses.user_timeline(screen_name = user)
