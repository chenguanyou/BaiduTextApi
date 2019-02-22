#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:13
# @User    : zhunishengrikuaile
# @File    : Lottery.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 彩票识别

import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

LOTTERY_URL = URL_LIST_URL['LOTTERY'] + '?access_token={}'.format(ACCESS_TOKEN)


class LotterySuper(object):
    pass


class Lottery(LotterySuper):

    def __init__(self, image=None, recognize_granularity='small'):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'recognize_granularity': recognize_granularity,
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postLottery(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空!'
        lottery = requests.post(url=LOTTERY_URL, headers=self.HEADER,
                                data=self.IMAGE_CONFIG)
        return lottery.json()
