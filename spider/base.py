#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:31
# File Name : base.py
import requests

import config

conf = config.conf.get('spider')


class BaseSpider(object):
    req = requests.Session()
    api_url = conf.get('api_url')
    jwt_token = conf.get('jwt_token')
    clan_tag = conf.get('clan_tag')

    req.headers = {
        'Authorization': 'Bearer ' + jwt_token
    }




