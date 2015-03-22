import json
import os

headers = {'content-length': '151106', 'x-rate-limit-reset': '1426988210', 'x-rate-limit-remaining': '175',
           'x-xss-protection': '1; mode=block', 'x-content-type-options': 'nosniff',
           'x-connection-hash': '7df1531c3b2137a15f3f5839eadc8618',
           'x-twitter-response-tags': 'BouncerCompliant',
           'cache-control': 'no-cache, no-store, must-revalidate, pre-check=0, post-check=0', 'status': '200',
           'content-disposition': 'attachment; filename=json.json',
           'set-cookie': 'guest_id=v1%3A142698798177591546; Domain=.twitter.com; Path=/; Expires=Tue, 21-Mar-2017 01:33:01 UTC',
           'expires': 'Tue, 31 Mar 1981 05:00:00 GMT', 'x-access-level': 'read',
           'last-modified': 'Sun, 22 Mar 2015 01:33:01 GMT', '-content-encoding': 'gzip', 'pragma': 'no-cache',
           'date': 'Sun, 22 Mar 2015 01:33:01 GMT', 'x-rate-limit-limit': '180', 'x-response-time': '262',
           'content-location': u'https://api.twitter.com/1.1/search/tweets.json?lang=en&count=50&oauth_nonce=80983227&oauth_timestamp=1426987981&oauth_consumer_key=eNjoWsl2E7Mme866VsPgxg&since=2015-03-20&oauth_signature_method=HMAC-SHA1&result_type=recent&q=iphone&oauth_version=1.0&oauth_token=153974650-yt58rLOoSriCyf5ctysmlHPbaYFiTrTrlo0U5xd9&oauth_body_hash=2jmj7l5rSw0yVb%2FvlWAYkK%2FYBwk%3D&oauth_signature=r1sdOG%2FwuXnFVGThP9KtSPuT2j0%3D&include_entities=0&until=2015-03-21',
           'x-transaction': '133784a9d6541ad2', 'strict-transport-security': 'max-age=631138519',
           'server': 'tsa_d', 'x-frame-options': 'SAMEORIGIN', 'content-type': 'application/json;charset=utf-8'}


with open(os.path.join(os.path.dirname(__file__), 'mock_response.json')) as data_file:
    data_file = json.load(data_file)
    body = json.dumps(data_file)

body_error = r'{"statuses" : "error"}'