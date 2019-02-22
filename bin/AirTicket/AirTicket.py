#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:35
# @User    : zhunishengrikuaile
# @File    : AirTicket.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# AirTicket
# 行程单识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

AIR_TICKET_URL = URL_LIST_URL['AIR_TICKET'] + '?access_token={}'.format(ACCESS_TOKEN)


class AirTicketSuper(object):
    pass


class AirTicket(AirTicketSuper):

    def __init__(self, image=None):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postAirTicket(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空!'
        airTicket = requests.post(url=AIR_TICKET_URL, headers=self.HEADER,
                                  data=self.IMAGE_CONFIG)
        return airTicket.json()
