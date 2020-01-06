# coding: utf-8
# Create by Annhuny On 2020-01-07 01:42
# File Name : redis_session.py
import redis

from config import conf


redis_cfg = conf.get('DB').get('redis')
r_session = redis.Redis(**{
    'host': redis_cfg.get('host'),
    'port': redis_cfg.get('port'),
    'password': redis_cfg.get('password')
})
