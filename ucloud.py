#!/usr/bin/python
import hmac
import json
import urllib
from hashlib import sha1

def request(parameters, apikey='', secretkey=''):
    url = 'https://api.ucloudbiz.olleh.com/server/v1/client/api'
    query = dict(apikey=apikey,
                 response='json')
    query.update(parameters)
    tmp_query = dict()
    for key, value in query.iteritems():
        tmp_query[urllib.quote(key)] = urllib.quote(value)
    command_string = []
    for key in sorted(tmp_query.keys()):
        command_string.append('%s=%s'%(key, tmp_query[key]))
    command_string = '&'.join(command_string).lower()
    query['signature'] = hmac.new(secretkey, command_string, sha1).digest().encode('base64')[:-1]
    url = '%s?%s' % (url, urllib.urlencode(query))
    response = urllib.urlopen(url).read()
    return json.loads(response)
