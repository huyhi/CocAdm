#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 17:15
# File Name : fetch_members_data.py

# example
# {
#     "tag": "#89Y0PLUV8",      // tag
#     "name": "二宝",            // 昵称
#     "role": "coLeader",       // 职位
#     "expLevel": 198,          // 等级
#     "league": {               // 联赛
#         "id": 29000017,
#         "name": "Champion League II",
#         "iconUrls": {
#             "small": "https://api-assets.clashofclans.com/leagues/72/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png",
#             "tiny": "https://api-assets.clashofclans.com/leagues/36/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png",
#             "medium": "https://api-assets.clashofclans.com/leagues/288/kLWSSyq7vJiRiCantiKCoFuSJOxief6R1ky6AyfB8q0.png"
#         }
#     },
#     "trophies": 3657,         // 奖杯🏆
#     "versusTrophies": 3901,   // 对抗赛奖杯🏆
#     "clanRank": 2,            // 部落内排名
#     "previousClanRank": 2,    // 部落内前排名
#     "donations": 11450,           // 捐兵
#     "donationsReceived": 10718    // 收兵
# }
import datetime

from DB.sqlalchemySession import session
from Models.models import FlowingData
from spider.clan import ClanSpider


def fetch_players_tag_list():
    members = ClanSpider.clan_members()
    return [member.get('tag') for member in members]


def fetch_player_flowing_data():
    players_tag_list = fetch_players_tag_list()
    for player_tag in players_tag_list:
        player_data = ClanSpider.player_information(playerTag=player_tag)
        player_data['datetimeTag'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session.add(FlowingData(**player_data))

    session.commit()
    return True




