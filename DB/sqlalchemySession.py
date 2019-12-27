#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 20:02
# File Name : sqlalchemySession.py

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接 TODO => 后续改成配置模式
engine = create_engine('mysql+mysqlconnector://root:Az@2323369194@118.178.180.53:3306/coc')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
