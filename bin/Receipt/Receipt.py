#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:37
# @User    : zhunishengrikuaile
# @File    : Receipt.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 通用票据识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

RECEIPT_URL = URL_LIST_URL['RECEIPT'] + '?access_token={}'.format(ACCESS_TOKEN)


class ReceiptSuper(object):
    pass


class Receipt(ReceiptSuper):
    '''
    异步接口获取ID
    @image
    '''

    def __init__(self, image=None, recognize_granularity='small', probability=True, accuracy='normal',
                 detect_direction=True):

        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'recognize_granularity': recognize_granularity,
            'probability': probability,
            'accuracy': accuracy,
            'detect_direction': detect_direction
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postReceipt(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        receipt = requests.post(url=RECEIPT_URL, headers=self.HEADER,
                                data=self.IMAGE_CONFIG)
        return receipt.json()
