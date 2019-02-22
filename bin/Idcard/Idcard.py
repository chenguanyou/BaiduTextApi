#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 15:04
# @User    : zhunishengrikuaile
# @File    : Idcard.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 身份证识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import URL_LIST_URL, LOCALHOST_PATH

ACCESS_TOKEN = AccessToken().getToken()['access_token']
IDCARD_URL = URL_LIST_URL['IDCARD'] + '?access_token={}'.format(ACCESS_TOKEN)


class IdcardSuper(object):
    pass


class Idcard(IdcardSuper):
    def __init__(self, image=None, detect_direction=True, id_card_side='front', detect_risk=False):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        self.IMAGE_CONFIG = {
            'detect_direction': detect_direction,
            'id_card_side': id_card_side,
            'detect_risk': detect_risk
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postIdcard(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        idcard = requests.post(url=IDCARD_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        return idcard.json()
