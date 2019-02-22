#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 09:47
# @User    : zhunishengrikuaile
# @File    : AccessToken.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装

# ACCESS_TOKEN获取
# ACCESS_TOKEN_URL用于获取ACCESS_TOKEN, POST请求,
# grant_type必须参数,固定为client_credentials,client_id必须参数,应用的API Key,client_secre 必须参数,应用的Secret Key.
import requests
from config.config import URL_LIST_URL


class AccessTokenSuper(object):
    pass


class AccessToken(AccessTokenSuper):
    def getToken(self):
        '''
        request post accesstoken
        :return:
        '''
        accessToken = requests.post(url=URL_LIST_URL['ACCESS_TOKEN_URL'])
        accessTokenJson = accessToken.json()
        if dict(accessTokenJson).get('error') == 'invalid_client':
            return '获取accesstoken错误，请检查API_KEY，SECRET_KEY是否正确！'
        return accessTokenJson
