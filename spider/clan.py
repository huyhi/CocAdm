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
        cls.api_url = '%s/%s/%s' % (cls.api_url, 'clans', quote(cls.clanTag, 'utf-8'))
        res = cls.req.get(cls.api_url)
        return res.json()

    @classmethod
    def clan_members(cls, **kwargs):
        # cls.api_url = '%s/%s/%s/%s' % (cls.api_url, 'clans', quote(cls.clanTag, 'utf-8'), 'members')
        # res = cls.req.get(cls.api_url)
        # return res.json().get('items', {})
        return [{
            "tag": "#89Y0PLUV8",
            "name": "二宝",
            "role": "coLeader",
            "expLevel": 198,
            "league": {
                "id": 29000017,
                "name": "Champion League II",
                "iconUrls": {
                    "small": "https://api-assets.clashofclans.com/leagues/72/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png",
                    "tiny": "https://api-assets.clashofclans.com/leagues/36/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png",
                    "medium": "https://api-assets.clashofclans.com/leagues/288/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png"
                }
            },
            "trophies": 3657,
            "versusTrophies": 3901,
            "clanRank": 2,
            "previousClanRank": 2,
            "donations": 11450,
            "donationsReceived": 10718
        }]

    @classmethod
    def player_information(cls, **kwargs):
        # player_tag = kwargs.get('playerTag', '')
        # cls.api_url = '%s/%s/%s' % (cls.api_url, 'players', quote(player_tag, 'utf-8'))
        # res = cls.req.get(cls.api_url)
        # res = res.json()
        with open(PROJECT_ROOT_DIR + '/json_example/player_information.json', 'r') as f:
            res = json.loads(f.read())

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


