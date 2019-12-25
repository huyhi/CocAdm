#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:56
# File Name : BasePreRequest.py
import os

import yaml
from django.utils.deprecation import MiddlewareMixin

import settings
from settings import PROJECT_ROOT_DIR, CFG_FILE_NAME


class BasePreRequestsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        cfg_file = os.path.join(PROJECT_ROOT_DIR, CFG_FILE_NAME)
        settings.cfg = yaml.load(open(cfg_file))
