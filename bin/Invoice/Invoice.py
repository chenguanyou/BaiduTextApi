#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:30
# @User    : zhunishengrikuaile
# @File    : Invoice.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 税务局通用机打发票识别
# Invoice
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

INVOICE_URL = URL_LIST_URL['INVOICE'] + '?access_token={}'.format(ACCESS_TOKEN)


class InvoiceSuper(object):
    pass


class Invoice(InvoiceSuper):

    def __init__(self, image=None, location=True):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'location': location,
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postInvoice(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空!'
        invoice = requests.post(url=INVOICE_URL, headers=self.HEADER,
                                data=self.IMAGE_CONFIG)
        return invoice.json()
