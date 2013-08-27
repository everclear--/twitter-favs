#!/usr/bin/env python
"""
https://dev.twitter.com/docs/api/1.1
"""
import twitter as tw

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


def load_api():
    t = tw.Twitter(
            auth=tw.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )
    return t

if __name__ == '__main__':
    t = load_api()

    COUNT = 200  # this is the max allowed
    max_id= None
    size = 1

    while size:
        if max_id:
            favs = t.favorites.list(count=COUNT, max_id=max_id)
        else:
            favs = t.favorites.list(count=COUNT)

        for fav in favs:
            text = fav['text']
            tweet_id = fav['id_str']
            created_at = fav['created_at']
            user_id = fav['user']['id_str']
            user_screen_name = fav['user']['screen_name']
            link_url = 'http://twitter.com/{}/statuses/{}'.format(user_id, tweet_id)
            max_id = int(tweet_id) - 1
            print text
            print "@{}".format(user_screen_name)
            print link_url
            print created_at
            print ''

        size = len(favs)
