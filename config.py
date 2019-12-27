#!/usr/bin/env python
# Create by Annhuny On 2019-12-27 16:17
# File Name : config.py
#
# 单例模式实现配置
import os

import yaml

from settings import PROJECT_ROOT_DIR, CFG_FILE_NAME


class ConfSingleton(object):

    _conf_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._conf_instance:
            with open(os.path.join(PROJECT_ROOT_DIR, CFG_FILE_NAME)) as cfg_file:
                cls._conf_instance = yaml.load(cfg_file)
        return cls._conf_instance


conf = ConfSingleton()


if __name__ == '__main__':
    print(conf)

