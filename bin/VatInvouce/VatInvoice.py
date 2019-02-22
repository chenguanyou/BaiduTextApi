#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:54
# @User    : zhunishengrikuaile
# @File    : VatInvoice.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 增值税发票识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']
VAT_INVOICE_URL = URL_LIST_URL['VAT_INVOICE'] + '?access_token={}'.format(ACCESS_TOKEN)


class VatInvoiceSuper(object):
    pass


class VatInvoice(VatInvoiceSuper):
    '''
    异步接口获取ID
    @image
    '''

    def __init__(self, image=None, accuracy='normal'):

        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'accuracy': accuracy,
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postVatInvoice(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        vatInvoice = requests.post(url=VAT_INVOICE_URL, headers=self.HEADER,
                                   data=self.IMAGE_CONFIG)
        return vatInvoice.json()
