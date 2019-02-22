#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 10:34
# @User    : zhunishengrikuaile
# @File    : VinCode.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# VinCode
# 车辆VIN码识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

VIN_CODE_URL = URL_LIST_URL['VIN_CODE'] + '?access_token={}'.format(ACCESS_TOKEN)


class VinCodeSuper(object):
    pass


class VinCode(VinCodeSuper):

    def __init__(self, image=None, imgDirection='setImgDirFlag'):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'imgDirection': imgDirection,
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postVinCode(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        vinCode = requests.post(url=VIN_CODE_URL, headers=self.HEADER,
                                data=self.IMAGE_CONFIG)
        return vinCode.json()
