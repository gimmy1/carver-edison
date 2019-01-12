import json
import unittest

from project.tests.base import BaseTestCase

from project import db
from project.api.models import Tweet

def add_tweet(title, name):
    tweet = Tweet(title=title, name=name)
    db.session.add(tweet)
    db.session.commit()
    return tweet

class TestTweets(BaseTestCase):
    """ Tests for the Tweets Service """
    def test_tweets(self):
        """ Ensure the /tweets route behaves correctly """
        response = self.client.get('/tweets/tweet')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('tweet', data['tweet'])
    
    def test_single_tweet(self):
        tweet = add_tweet(title='Carver Edison', name='Prakash Sinha')
        # print(tweet.id)
        with self.client:
            response = self.client.get(f'/tweets/{tweet.id}')
            data = json.loads(response.data.decode())
            self.assertIn('Carver Edison', data['title'])
            self.assertIn('Prakash Sinha', data['name'])
        
    def test_single_tweet_does_not_exist(self):
        """ Ensure error is thrown without id """
        with self.client: 
            response = self.client.get(f'/tweets/does_not_exist')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Does not exist', data['message'])
    
    def test_all_tweets(self):
        """ Get all tweets """
        add_tweet(title='Carver Edison', name='Prakash Sinha')
        add_tweet(title='Software Engineer', name='Gamal Ali')
        with self.client: 
            response = self.client.get(f'/tweets/')
            data = json.loads(response.data.decode())
            # import pdb; pdb.set_trace()
            self.assertIn('Prakash Sinha', data['tweets'][0]['name'])
            self.assertIn('Gamal Ali', data['tweets'][1]['name'])


            





if __name__ == '__main__':
    unittest.main()
        