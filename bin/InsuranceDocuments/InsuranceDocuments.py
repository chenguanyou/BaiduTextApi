#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:22
# @User    : zhunishengrikuaile
# @File    : InsuranceDocuments.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# InsuranceDocuments
# 保单识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

INSURANCE_DOCUMENTS_URL = URL_LIST_URL['INSURANCE_DOCUMENTS'] + '?access_token={}'.format(ACCESS_TOKEN)


class InsuranceDocumentsSuper(object):
    pass


class InsuranceDocuments(InsuranceDocumentsSuper):

    def __init__(self, image=None, rkv_business='rue'):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'rkv_business': rkv_business,
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postInsuranceDocuments(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空!'
        insuranceDocuments = requests.post(url=INSURANCE_DOCUMENTS_URL, headers=self.HEADER,
                                           data=self.IMAGE_CONFIG)
        return insuranceDocuments.json()
