import get_twitter_data
from httplib2 import Response
import logging
from mock import patch
from unittest import TestCase
import os

def get_mockup_result():
    from test_resources import body, headers

    return Response(headers), body


def get_mock_error():
    from test_resources import headers, body_error

    return Response(headers), body_error


def mock_request(self, uri, method="GET", body=None, headers=None, redirections=1, connection_type=None):
    actions = {'https://api.twitter.com/1.1/error': get_mock_error,
               'https://api.twitter.com/1.1/search/tweets.json?': get_mockup_result}
    for action_trigger, action in actions.iteritems():
        if action_trigger in uri:
            return action()

    logging.error("No response for '%s'" % uri)
    return Response({}), ''


class TestGetTwitterData(TestCase):
    def setUp(self):
        patcher = patch('oauth2.Client.request', mock_request)
        patcher.start()
        self.twitterData = get_twitter_data.TwitterData(os.path.join(os.path.dirname(__file__), '../config.json'))

    def test_raw_content(self):
        import urllib

        url = 'https://api.twitter.com/1.1/search/tweets.json?'
        data = {'q': 'iphone', 'lang': 'en', 'result_type': 'recent', 'count': 50, 'include_entities': 0}
        params = {}

        for key, value in params.iteritems():
            data[key] = value

        url += urllib.urlencode(data)
        headers, content = self.twitterData.oauth_req(url)
        self.assertEquals(headers['content-length'], '151106')


    def test_get_twitter_data(self):
        expects1 = u'This a Mockup response'
        expects2 = "iPhone?"
        keyword = 'iphone'
        time = 'today'
        tweets = self.twitterData.getTwitterData(keyword, time)
        tweets = tweets[0]
        self.assertEqual(expects1, tweets[0])
        self.assertEqual(expects2, tweets[1])
