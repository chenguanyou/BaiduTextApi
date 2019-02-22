#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 15:27
# @User    : zhunishengrikuaile
# @File    : GeneralEnhanced.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 通用文字识别（含生僻字版）
# URL参数：
## access_token	调用AccessToken模块获取
# Headers参数
## 参数：Content-Type	，值：application/x-www-form-urlencoded
# Body请求参数：
## 参数：image，	                    是否必选：和url二选一，	        类型：string，  	可选值范围：null	                                                            说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
## 参数：url，	                    是否必选：和image二选一，	    类型：string，  	可选值范围：null	                                                            说明：图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
## 参数：language_type，	            是否必选：false，	            类型：string，  	可选值范围：[CHN_ENG、ENG、POR、FRE、GER、ITA、SPA、RUS、JAP、KOR]	            说明：[识别语言类型，默认为CHN_ENG。可选值包括： - CHN_ENG：中英文混合； - ENG：英文； - POR：葡萄牙语； - FRE：法语； - GER：德语； - ITA：意大利语； - SPA：西班牙语； - RUS：俄语； - JAP：日语； - KOR：韩语]
## 参数：detect_direction，	        是否必选：false，	            类型：string，  	可选值范围：[true、false]	                                                    说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
## 参数：detect_language，	        是否必选：FALSE，	            类型：string，  	可选值范围：[true、false]	                                                    说明：是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
## 参数：probability，	            是否必选：false，	            类型：string，  	可选值范围：[true、false]
# ---------------------------------------------------------------------------------------
# 返回说明
## 字段：direction，	                是否必选：否	    类型：int32，	            说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
## 字段：log_id，	                    是否必选：是	    类型：uint64，	        说明：唯一的log id，用于问题定位
## 字段：words_result，	            是否必选：是	    类型：array()，	        说明：识别结果数组
## 字段：words_result_num，	        是否必选：是	    类型：uint32，	        说明：识别结果数，表示words_result的元素个数
## 字段：+words，	                    是否必选：否	    类型：string，	        说明：识别结果字符串
## 字段：probability，	            是否必选：否	    类型：object，	        说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值

import os
import base64
import requests
from config.config import LOCALHOST_PATH, URL_LIST_URL
from bin.AccessToken.AccessToken import AccessToken

ACCESS_TOKEN = AccessToken().getToken()['access_token']
GENNERAL_ENHANCED_URL = URL_LIST_URL['GENNERAL_ENHANCED'] + '?access_token={}'.format(ACCESS_TOKEN)


class GeneralEnhancedSuper(object):
    pass


class GenneralEnhanced(GeneralEnhancedSuper):
    def __init__(self, image=None, url=None, language_type='CHN_ENG', detect_direction=True, detect_language=True,
                 probability=True):

        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'language_type': language_type,
            'detect_direction': detect_direction,
            'detect_language': detect_language,
            'probability': probability
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

    def postGenneralEnhanced(self):
        try:
            generalEnhanced = requests.post(url=GENNERAL_ENHANCED_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        except AttributeError:
            return 'image和url参数任选其一！'
        return generalEnhanced.json()
