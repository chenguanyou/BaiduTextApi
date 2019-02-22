#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 15:41
# @User    : zhunishengrikuaile
# @File    : BusinessLicense.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 营业执照识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

BUSINESS_LICENSE_URL = URL_LIST_URL['BUSINESS_LICENSE'] + '?access_token={}'.format(ACCESS_TOKEN)


class BusinessLicenseSuper(object):
    pass


class BusinessLicense(BusinessLicenseSuper):
    def __init__(self, image=None, detect_direction=True, accuracy='high'):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'detect_direction': detect_direction,
            'accuracy': accuracy
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postBusinessLicense(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        busunessLincense = requests.post(url=BUSINESS_LICENSE_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        return busunessLincense.json()
