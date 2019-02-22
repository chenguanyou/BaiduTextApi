#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 10:21
# @User    : zhunishengrikuaile
# @File    : FormOrc.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 表格文字识别(异步接口)
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

FORM_ORC_REQUEST_URL = URL_LIST_URL['FORM_ORC_REQUEST'] + '?access_token={}'.format(ACCESS_TOKEN)
FORM_ORC_GET_REQUEST_RESULT_URL = URL_LIST_URL['FORM_ORC_GET_REQUEST_RESULT'] + '?access_token={}'.format(ACCESS_TOKEN)


class FormOrcRequestSuper(object):
    pass


class FormOrcRequest(FormOrcRequestSuper):
    '''
    异步接口获取ID
    @image
    '''

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

    def postFormOrcRequest(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        formOrcRequest = requests.post(url=FORM_ORC_REQUEST_URL, headers=self.HEADER,
                                       data=self.IMAGE_CONFIG)
        return formOrcRequest.json()


class FormOrcGetRequestResult(FormOrcRequestSuper):

    def __init__(self, request_id, result_type=None):
        '''
        request_id	是	string	-	发送表格文字识别请求时返回的request id
        result_type	否	string	-	期望获取结果的类型，取值为“excel”时返回xls文件的地址，取值为“json”时返回json格式的字符串,默认为”excel”
        :param request_id:
        :param result_type:
        '''
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        self.IMAGE_CONFIG = {
            'request_id': request_id,
            'result_type': result_type
        }

    def postFormOrcGetRequestResult(self):
        formOrcGetRequestResult = requests.post(url=FORM_ORC_GET_REQUEST_RESULT_URL, headers=self.HEADER,
                                                data=self.IMAGE_CONFIG)
        return formOrcGetRequestResult.json()
