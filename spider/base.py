#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:31
# File Name : base.py

import requests


class BaseSpider(object):
    def __init__(self):
        self.req = requests.Session()
        self.api_url = 'https://api.clashofclans.com/v1'
        # 后续尝试改成配置的形式
        self.jwt_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImI1ZjMxMjM0LTEwYmItNDczMC1hZjFkLWQ5NTE4OWRlNDVmMCIsImlhdCI6MTU3NzI1NTgyNCwic3ViIjoiZGV2ZWxvcGVyLzAwN2Y2MjEwLWEyODktMDA4YS04YWVhLWYwZTNhYmQ2NTVlYiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0OS4xMjkuMTEwLjExMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.T-bbdPLjwf-pgH0qWxlOAYhiVzL0ipU286dKx2w8Hdlq4aWZW-USuKmyulQYM5HCA5AaXQXUZ5NWQdOV1RyLtg'
        self.clanTag = '#PCCR9LQU'

        self.req.headers = {
            'Authorization': 'Bearer ' + self.jwt_token
        }




