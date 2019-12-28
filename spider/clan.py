#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:30
# File Name : clan.py
import json
from urllib.parse import quote

from settings import PROJECT_ROOT_DIR
from spider.base import BaseSpider


class ClanSpider(BaseSpider):

    @classmethod
    def clan_detail(cls, **kwargs):
        api_url = '%s/%s/%s' % (cls.api_url, 'clans', quote('#' + cls.clan_tag, 'utf-8'))
        res = cls.req.get(api_url)
        return res.json()

    @classmethod
    def clan_members(cls, **kwargs):
        api_url = '%s/%s/%s/%s' % (cls.api_url, 'clans', quote('#' + cls.clan_tag, 'utf-8'), 'members')
        res = cls.req.get(api_url)
        return res.json().get('items', {})

    @classmethod
    def player_information(cls, **kwargs):
        player_tag = kwargs.get('player_tag', '')
        api_url = '%s/%s/%s' % (cls.api_url, 'players', quote(player_tag, 'utf-8'))
        res = cls.req.get(api_url).json()
        # with open(PROJECT_ROOT_DIR + '/json_example/player_information.json', 'r') as f:
        #     res = json.loads(f.read())

        active_index_arrays = ['Gold Grab', 'Elixir Escapade', 'Heroic Heist']
        active_index_dict = {}
        for item in res.get('achievements', {}):
            if item['name'] in active_index_arrays:
                active_index_dict[item['name']] = item['value']

        return {
            'tag': res.get('tag'),
            'expLevel': res.get('expLevel'),
            'trophies': res.get('trophies'),
            'versusTrophies': res.get('versusTrophies'),
            'attackWins': res.get('attackWins'),
            'donations': res.get('donations'),
            'donationsReceived': res.get('donationsReceived'),
            'gold': active_index_dict.get('Gold Grab'),
            'elixir': active_index_dict.get('Elixir Escapade'),
            'darkElixir': active_index_dict.get('Heroic Heist')
        }


