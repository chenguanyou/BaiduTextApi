#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 11:35
# @User    : zhunishengrikuaile
# @File    : WebImage.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 网络图片文字识别
import os
import base64
import requests
from config.config import LOCALHOST_PATH, URL_LIST_URL
from bin.AccessToken.AccessToken import AccessToken

ACCESS_TOKEN = AccessToken().getToken()['access_token']
WEB_IMAGE_URL = URL_LIST_URL['WEB_IMAGE'] + '?access_token={}'.format(ACCESS_TOKEN)


class WebImageSuper(object):
    pass


class WebImage(WebImageSuper):
    def __init__(self, image=None, url=None, detect_direction=True, detect_language=True):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'detect_direction': detect_direction,
            'detect_language': detect_language,
        }

        if image is None:
            if url is not None:
                self.IMAGE_CONFIG['url'] = url
        elif url is None:
            imagePath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagePath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as image1:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(image1.read())
        elif url and image is not None:
            self.IMAGE_CONFIG['url'] = url

    def postWebImage(self):
        try:
            webImage = requests.post(url=WEB_IMAGE_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        except AttributeError:
            return 'image和url参数任选其一！'
        return webImage.json()
