#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 12:36
# @User    : zhunishengrikuaile
# @File    : accurateBase.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 通用文字识别(高精度版)
# URL参数：
## access_token	调用AccessToken模块获取
# Headers参数
## 参数：Content-Type	，值：application/x-www-form-urlencoded
# Body请求参数
## 参数：image，	            是否必选：true，	类型：string，  	可选值范围：null	            说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
## 参数：detect_direction，	是否必选：false，	类型：string，  	可选值范围：[true、false]	    说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
## 参数：probability，	    是否必选：false，	类型：string，  	可选值范围：[true、false]	    说明：是否返回识别结果中每一行的置信度
# -----------------------------------------------------------------------
# 返回说明
## 字段：direction，	            是否必选：否	    类型：int32，	    说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
## 字段：log_id，	                是否必选：是	    类型：uint64，	说明：唯一的log id，用于问题定位
## 字段：words_result，	        是否必选：是	    类型：array()，	说明：识别结果数组
## 字段：words_result_num，	    是否必选：是	    类型：uint32，	说明：识别结果数，表示words_result的元素个数
## 字段：+words，	                是否必选：否	    类型：string，	说明：识别结果字符串
## 字段：probability，	        是否必选：否	    类型：object	，	说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值

import os
import base64
import requests
from config.config import URL_LIST_URL, LOCALHOST_PATH
from bin.AccessToken.AccessToken import AccessToken

ACCESS_TOKEN = AccessToken().getToken()
ACCURATE_BASIC_URL = URL_LIST_URL['ACCURATE_BASIC'] + '?access_token={}'.format(ACCESS_TOKEN['access_token'])


class AccurateBaseSuper(object):
    pass


class AccurateBase(object):
    def __init__(self, image=None, detect_direction=True, probability=True):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.IMAGE_CONFIG = {
            'image': None,
            'detect_direction': detect_direction,
            'probability': probability
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postAccurateBase(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        accurateBase = requests.post(url=ACCURATE_BASIC_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        return accurateBase.json()
