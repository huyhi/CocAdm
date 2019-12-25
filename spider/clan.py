#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:30
# File Name : clan.py
from urllib.parse import urlencode, quote

from spider.base import BaseSpider


class ClanSpider(BaseSpider):

    def clanDetail(self, **kwargs):
        self.api_url = '%s/%s/%s' % (self.api_url, 'clans', quote(kwargs.get('clanTag'), 'utf-8'))
        res = self.req.get(self.api_url)
        return res.json()




