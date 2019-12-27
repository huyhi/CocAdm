#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:31
# File Name : base.py

import requests


class BaseSpider(object):
    req = requests.Session()
    api_url = 'https://api.clashofclans.com/v1'
    # 后续尝试改成配置的形式
    jwt_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImU4OWIzODU1LWQyNmQtNDc4Yi1hZGVkLTA5MWNjZDIxMjNkMSIsImlhdCI6MTU3NzM3MjI5NSwic3ViIjoiZGV2ZWxvcGVyLzAwN2Y2MjEwLWEyODktMDA4YS04YWVhLWYwZTNhYmQ2NTVlYiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExNy4xMzYuNDUuMTAwIl0sInR5cGUiOiJjbGllbnQifV19.BWfuHF44UY0thrLKWRKqky3C7J96BIRMNnEZY5I_V66gDdW7y5DNqO3R65lVqzkD8DnLboEkol-xMVQk6gtrkg'
    clanTag = '#PCCR9LQU'
    test_member_id = '#22GU0VCQR'

    req.headers = {
        'Authorization': 'Bearer ' + jwt_token
    }




