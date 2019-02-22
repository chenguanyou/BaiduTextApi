#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 08:58
# @User    : zhunishengrikuaile
# @File    : config.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
# 配置文件
'''
应用ID: 14348843
应用API_KEY: wc68dHtiY9mwuD7980EXr1I2
应用SECRET_KEY: dCaMG095LvB9pdtRqbn5eWP4RFSLnj74
'''
import os

# from bin.AccessToken.GetToken.GetAccesToken import getname

#
ACCESS_TOKEN = ''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ID,KEY的配置信息
INFO_CONFIG = {
    'ID': '14348843',
    'API_KEY': 'wc68dHtiY9mwuD7980EXr1I2',
    'SECRET_KEY': 'dCaMG095LvB9pdtRqbn5eWP4RFSLnj74'
}

# 本地路径配置
LOCALHOST_PATH = {
    'PATH': os.path.join(BASE_DIR, 'test/img/')
}

# URL配置
URL_LIST_URL = {
    # ACCESS_TOKEN_URL用于获取ACCESS_TOKEN, POST请求,
    #  grant_type必须参数,固定为client_credentials,client_id必须参数,应用的API Key,client_secre 必须参数,应用的Secret Key.
    'ACCESS_TOKEN_URL': 'https://aip.baidubce.com/oauth/2.0/token?' + 'grant_type=client_credentials&client_id={API_KEYS}&client_secret={SECRET_KEYS}&'.format(
        API_KEYS=INFO_CONFIG['API_KEY'], SECRET_KEYS=INFO_CONFIG['SECRET_KEY']),
    # 通用文字识别, 接口POST请求,
    # url参数：
    ## access_token 调用AccessToken模块获取
    # Header参数：
    ## Content-Type: application/x-www-form-urlencoded
    # Body中的请求参数：
    ## 参数：image	，              是否必选：和url二选一，   类型：string，  可选值范围：null，                                               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    ## 参数：url	，              是否必选：和image二选一， 类型：string，  可选值范围：null，                                               说明：图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
    ## 参数：language_type	，      是否必选：false，        类型：string，  可选值范围：[CHN_ENG、ENG、POR、FRE、GER、ITA、SPA、RUS、JAP、KOR], 说明：识别语言类型，默认为CHN_ENG。可选值包括： [- CHN_ENG：中英文混合； - ENG：英文； - POR：葡萄牙语； - FRE：法语； - GER：德语； - ITA：意大利语； - SPA：西班牙语； - RUS：俄语； - JAP：日语； - KOR：韩语]
    ## 参数：detect_direction	，  是否必选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
    ## 参数：detect_language，    是否可选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
    ## 参数：probability，        是否可选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否返回识别结果中每一行的置信度
    # ------------------------------------------------------------------
    # 返回参数
    ## 字段：direction，	            是否必选：否	    类型：int32，	    说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：log_id，	                是否必选：是	    类型：uint64，	说明：唯一的log id，用于问题定位
    ## 字段：words_result，	        是否必选：是	    类型：array()，	说明：识别结果数组
    ## 字段：words_result_num，	    是否必选：是	    类型：uint32，	说明：识别结果数，表示words_result的元素个数
    ## 字段：+words，	                是否必选：否	    类型：string，	说明：识别结果字符串
    ## 字段：probability，	        是否必选：否	    类型：object	，	说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'GENERAL_BASIC': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
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
    'ACCURATE_BASIC': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic',
    # 通用文字识别（含位置信息版）
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，	                    是否必选：和url二选一，	    类型：string，  	可选值范围：null	                                                            说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    ## 参数：url，	                    是否必选：和image二选一，	类型：string，  	可选值范围：null	                                                            说明：图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
    ## 参数：recognize_granularity，	    是否必选：false，	        类型：string，  	可选值范围：[big、small]	                                                    说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：language_type，	            是否必选：false，	        类型：string，  	可选值范围：[CHN_ENG、ENG、POR、FRE、GER、ITA、SPA、RUS、JAP、KOR]	            说明：识别语言类型，默认为CHN_ENG。可选值包括： - CHN_ENG：中英文混合； - ENG：英文； - POR：葡萄牙语； - FRE：法语； - GER：德语； - ITA：意大利语； - SPA：西班牙语； - RUS：俄语； - JAP：日语； - KOR：韩语
    ## 参数：detect_direction，	        是否必选：false，	        类型：string，  	可选值范围：[true、false]	                                                    说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
    ## 参数：detect_language，	        是否必选：FALSE，	        类型：string，  	可选值范围：[true、false]	 	                                                说明：是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
    ## 参数：vertexes_location，	        是否必选：FALSE，	        类型：string，  	可选值范围：[true、false]	 	                                                说明：是否返回文字外接多边形顶点位置，不支持单字位置。默认为false
    ## 参数：probability，	            是否必选：false，	        类型：string，  	可选值范围：[true、false]	 	                                                说明：是否返回识别结果中每一行的置信度
    # ---------------------------------------------------------------------------------------
    # 返回说明
    ## 字段：direction，	                    是否必选：否	    类型：int32，	        说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：log_id，	                        是否必选：是		类型：uint64，	    说明：唯一的log id，用于问题定位
    ## 字段：words_result，	                是否必选：是	    类型：array()，	    说明：定位和识别结果数组
    ## 字段：words_result_num，	            是否必选：是	    类型：uint32，	    说明：识别结果数，表示words_result的元素个数
    ## 字段：+vertexes_location，	            是否必选：否	    类型：array()，	    说明：当前为四个顶点: 左上，右上，右下，左下。当vertexes_location=true时存在
    ## 字段：++x，	                        是否必选：是	    类型：uint32，	    说明：水平坐标（坐标0点为左上角）
    ## 字段：++y，	                        是否必选：是	    类型：uint32，	    说明：垂直坐标（坐标0点为左上角）
    ## 字段：+location，	                    是否必选：是	    类型：array()，	    说明：位置数组（坐标0点为左上角
    ## 字段：++left，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：++top，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：++width，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形的宽度
    ## 字段：++height，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形的高度
    ## 字段：+words，	                        是否必选：否	    类型：string，	    说明：识别结果字符串
    ## 字段：+chars，	                        是否必选：否	    类型：array()	，	    说明：单字符结果，recognize_granularity=small时存在
    ## 字段：++location，	                    是否必选：是	    类型：array()，	    说明：位置数组（坐标0点为左上角）
    ## 字段：+++left，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：+++top，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：+++width，	                    是否必选：是		类型：uint32，	    说明：表示定位定位位置的长方形的宽度
    ## 字段：+++height，	                    是否必选：是		类型：uint32，	    说明：表示位置的长方形的高度
    ## 字段：++char，	                        是否必选：是		类型：string，	    说明：单字符识别结果
    ## 字段：probability，	                是否必选：否	    类型：object，	    说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'GENERAL': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general',
    # 通用文字识别（含位置高精度版）
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，	                    是否必选：和url二选一，	    类型：string，  	可选值范围：null	         说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    ## 参数：recognize_granularity，	    是否必选：false，	        类型：string，  	可选值范围：[big、small]    说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：detect_direction，	        是否必选：false，	        类型：string，  	可选值范围：[true、false]	 说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
    ## 参数：vertexes_location，	        是否必选：FALSE，	        类型：string，  	可选值范围：[true、false]	 说明：是否返回文字外接多边形顶点位置，不支持单字位置。默认为false
    ## 参数：probability，	            是否必选：false，	        类型：string，  	可选值范围：[true、false]	 说明：是否返回识别结果中每一行的置信度
    # ---------------------------------------------------------------------------------------
    # 返回说明
    ## 字段：direction，	                    是否必选：否	    类型：int32，	        说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：log_id，	                        是否必选：是		类型：uint64，	    说明：唯一的log id，用于问题定位
    ## 字段：words_result，	                是否必选：是	    类型：array()，	    说明：定位和识别结果数组
    ## 字段：words_result_num，	            是否必选：是	    类型：uint32，	    说明：识别结果数，表示words_result的元素个数
    ## 字段：+vertexes_location，	            是否必选：否	    类型：array()，	    说明：当前为四个顶点: 左上，右上，右下，左下。当vertexes_location=true时存在
    ## 字段：++x，	                        是否必选：是	    类型：uint32，	    说明：水平坐标（坐标0点为左上角）
    ## 字段：++y，	                        是否必选：是	    类型：uint32，	    说明：垂直坐标（坐标0点为左上角）
    ## 字段：+location，	                    是否必选：是	    类型：array()，	    说明：位置数组（坐标0点为左上角
    ## 字段：++left，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：++top，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：++width，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形的宽度
    ## 字段：++height，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形的高度
    ## 字段：+words，	                        是否必选：否	    类型：string，	    说明：识别结果字符串
    ## 字段：+chars，	                        是否必选：否	    类型：array()	，	    说明：单字符结果，recognize_granularity=small时存在
    ## 字段：++location，	                    是否必选：是	    类型：array()，	    说明：位置数组（坐标0点为左上角）
    ## 字段：+++left，	                    是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：+++top，	                        是否必选：是	    类型：uint32，	    说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：+++width，	                    是否必选：是		类型：uint32，	    说明：表示定位定位位置的长方形的宽度
    ## 字段：+++height，	                    是否必选：是		类型：uint32，	    说明：表示位置的长方形的高度
    ## 字段：++char，	                        是否必选：是		类型：string，	    说明：单字符识别结果
    ## 字段：probability，	                是否必选：否	    类型：object，	    说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'ACCURATE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate',
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
    'GENNERAL_ENHANCED': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_enhanced',
    # 网络图片文字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，	                    是否必选：和url二选一，	        类型：string，  	可选值范围：null	                                                            说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    ## 参数：url，	                    是否必选：和image二选一，	    类型：string，  	可选值范围：null	                                                            说明：图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
    ## 参数：detect_direction	，  是否必选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
    ## 参数：detect_language，    是否可选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
    # ---------------------------------------------------------------------------------------
    # 返回说明
    ## 字段：direction，	                是否必选：否	    类型：int32，	            说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：log_id，	                    是否必选：是	    类型：uint64，	        说明：唯一的log id，用于问题定位
    ## 字段：words_result，	            是否必选：是	    类型：array()，	        说明：识别结果数组
    ## 字段：words_result_num，	        是否必选：是	    类型：uint32，	        说明：识别结果数，表示words_result的元素个数
    ## 字段：+words，	                    是否必选：否	    类型：string，	        说明：识别结果字符串
    ## 字段：probability，	            是否必选：否	    类型：object，	        说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'WEB_IMAGE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage',
    # 手写文字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                   是否必选：是	，           类型：string，    可选值范围：NULL，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：recognize_granularity，   是否必选：false，        类型：string，    可选值范围：[big、small]，           说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：words_type，              是否必选：false，        类型：string，    可选值范围：[默认/number]，          说明：words_type=number:手写数字识别；无此参数或传其它值 默认手写通用识别（目前支持汉字和英文）
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	                是否必选：是	    类型：uint64，	            说明：唯一的log id，用于问题定位
    ## 字段：words_result_num，	    是否必选：是	    类型：uint32，	            说明：识别结果数，表示words_result的元素个数
    ## 字段：words_result，	        是否必选：是	    类型：array()	，	            说明：定位和识别结果数组
    ## 字段：location，	            是否必选：是	    类型：object，	            说明：位置数组（坐标0点为左上角）
    ## 字段：left，	                是否必选：是	    类型：uint32	，	            说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的宽度
    ## 字段：height，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的高度
    ## 字段：words，	                是否必选：是	    类型：string，	            说明：识别结果字符串
    ## 字段：chars，	                是否必选：否	    类型：array()，	            说明：单字符结果，recognize_granularity=small时存在
    ## 字段：location，	            是否必选：是	    类型：array()	，	            说明：位置数组（坐标0点为左上角）
    ## 字段：left，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	                是否必选：是	    类型：uint32，	            说明：表示定位定位位置的长方形的宽度
    ## 字段：height，	                是否必选：是	    类型：uint32，	            说明：表示位置的长方形的高度
    ## 字段：char，	                是否必选：是	    类型：string，	            说明：单字符识别结果
    ## 字段：probability，	        是否必选：否	    类型：object，	            说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'HANDWRITING': 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting',
    # 身份证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：detect_direction，              是否必选：false，       类型：string，    可选值范围：[true、false]，          说明：是否检测图像旋转角度，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测旋转角度并矫正识别； - false：不检测旋转角度，针对摆放情况不可控制的情况建议本参数置为true。
    ## 参数：id_card_side，                  是否必选：true，        类型：string，    可选值范围：[front、back]，          说明：front：身份证含照片的一面；back：身份证带国徽的一面
    ## 参数：image，                         是否必选：true，        类型：string，    可选值范围：null，                   说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：detect_risk，                   是否必选：false，       类型：string，    可选值范围：[true,false]，           说明：是否开启身份证风险类型(身份证复印件、临时身份证、身份证翻拍、修改过的身份证)功能，默认不开启，即：false。可选值:true-开启；false-不开启
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：direction，	            是否必选：否	    类型：int32，	                说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：image_status，	        是否必选：是	    类型：string，	            说明：normal-识别正常reversed_side-身份证正反面颠倒non_idcard-上传的图片中不包含身份证blurred-身份证模糊other_type_card-其他类型证照over_exposure-身份证关键字段反光或过曝over_dark-身份证欠曝（亮度过低）unknown-未知状态
    ## 字段：risk_type，	            是否必选：否	    类型：string，	            说明：输入参数 detect_risk = true 时，则返回该字段识别身份证类型: normal-正常身份证；copy-复印件；temporary-临时身份证；screen-翻拍；unknown-其他未知情况
    ## 字段：edit_tool，	            是否必选：否	    类型：string，	            说明：如果参数 detect_risk = true 时，则返回此字段。如果检测身份证被编辑过，该字段指定编辑软件名称，如:Adobe Photoshop CC 2014 (Macintosh),如果没有被编辑过则返回值无此参数
    ## 字段：log_id，	                是否必选：是	    类型：uint64，	            说明：唯一的log id，用于问题定位
    ## 字段：words_result，	        是否必选：是	    类型：array()，	            说明：定位和识别结果数组
    ## 字段：words_result_num，	    是否必选：是	    类型：uint32，	            说明：识别结果数，表示words_result的元素个数
    ## 字段：+location，	            是否必选：是	    类型：array()	，	            说明：位置数组（坐标0点为左上角）
    ## 字段：++left，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：++top，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：++width，	            是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的宽度
    ## 字段：++height，	            是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的高度
    ## 字段：+words，	                是否必选：是	    类型：string，	            说明：识别结果字符串
    'IDCARD': 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard',
    # 银行卡识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：true，        类型：string，    可选值范围：null，                   说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：uint64，	                说明：请求标识码，随机数，唯一。
    ## 字段：result，	            是否必选：是	    类型：object，	                说明：返回结果
    ## 字段：+bank_card_number，	是否必选：是	    类型：string，	                说明：银行卡卡号
    ## 字段：+bank_name，	        是否必选：是	    类型：string，	                说明：银行名，不能识别时为空
    ## 字段：+bank_card_type，	是否必选：是	    类型：uint32，	                说明：银行卡类型，0:不能识别; 1: 借记卡; 2: 信用卡
    'BANK_CARD': 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard',
    # 营业执照识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：detect_direction，              是否必选：FALSE，        类型：string，    可选值范围：null，                   说明：可选值 true,false是否检测图像朝向，默认不检测，即：false。可选值包括true - 检测朝向；false - 不检测朝向。朝向是指输入图像是正常方向、逆时针旋转90/180/270度
    ## 参数：accuracy，                      是否必选：FALSE，        类型：string，    可选值范围：null，                   说明：可选值：normal,high参数选normal或为空使用快速服务；选择high使用高精度服务，但是时延会根据具体图片有相应的增加
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	        是否必选：是	    类型：uint64，	                说明：请求标识码，随机数，唯一。
    ## 字段：words_result_num是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：words_result，	是否必选：是	    类型：array()，	                说明：识别结果数组
    ## 字段：left，	        是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	        是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	        是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形的宽度
    ## 字段：height，	        是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形的高度
    ## 字段：words，	        是否必选：是	    类型：string，	                说明：识别结果字符串
    'BUSINESS_LICENSE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/business_license',
    # 护照识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	        是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：words_result_num是否必选：是	    类型：uint32，	                说明：识别结果数，表示words_result的元素个数
    ## 字段：words_result，	是否必选：是	    类型：array()，	                说明：定位和识别结果数组
    ## 字段：-location，	    是否必选：是	    类型：uint32，	                说明：水平坐标
    ## 字段：-words，	        是否必选：是	    类型：string，	                说明：识别内容
    'PASSPORT': 'https://aip.baidubce.com/rest/2.0/ocr/v1/passport',
    # 名片识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	        是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：words_result_num是否必选：是	    类型：uint32，	                说明：识别结果数，表示words_result的元素个数
    ## 字段：words_result，	是否必选：是	    类型：array()，	                说明：定位和识别结果数组
    'BUSUNESS_CARD': 'https://aip.baidubce.com/rest/2.0/ocr/v1/business_card',
    # 户口本识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	        是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：BirthAddress    是否必选：是	    类型：string，	                说明：出生地
    ## 字段：Birthday，	    是否必选：是	    类型：string，	                说明：生日
    ## 字段：CardNo，	        是否必选：是	    类型：string，	                说明：身份证号
    ## 字段：Name            是否必选：是	    类型：string，	                说明：姓名
    ## 字段：Nation，	        是否必选：是	    类型：string，	                说明：民族
    ## 字段：Relationship，	是否必选：是	    类型：string，	                说明：与户主关系
    ## 字段：Sex             是否必选：是	    类型：string，	                说明：性别
    'HOUSEHOLD_REGISTER': 'https://aip.baidubce.com/rest/2.0/ocr/v1/household_register',
    # 出生医学证明识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：BabyBirthday，	    是否必选：是	    类型：string，	                说明：出生时间
    ## 字段：BabyName            是否必选：是	    类型：string，	                说明：姓名
    ## 字段：BabySex，	        是否必选：是	    类型：string，	                说明：性别
    ## 字段：Code                是否必选：是	    类型：string，	                说明：出生证编号
    ## 字段：FatherName，	        是否必选：是	    类型：string，	                说明：父亲姓名
    ## 字段：MotherName，	        是否必选：是	    类型：string，	                说明：母亲姓名
    'BIRTH_CERTIFICATE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/birth_certificate',
    # 港澳通行证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：Address，	        是否必选：是	    类型：string，	                说明：签发地点
    ## 字段：Birthday            是否必选：是	    类型：string，	                说明：出生日期
    ## 字段：CardNum，	        是否必选：是	    类型：string，	                说明：卡号
    ## 字段：NameChn             是否必选：是	    类型：string，	                说明：姓名
    ## 字段：NameEng，	        是否必选：是	    类型：string，	                说明：姓名拼音
    ## 字段：Sex，	            是否必选：是	    类型：string，	                说明：性别
    ## 字段：ValidDate，	        是否必选：是	    类型：string，	                说明：有效期限
    'HK_MACAU_EXITENTRPERMIT': 'https://aip.baidubce.com/rest/2.0/ocr/v1/HK_Macau_exitentrypermit',
    # 台湾通行证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：Address，	        是否必选：是	    类型：string，	                说明：签发地点
    ## 字段：Birthday            是否必选：是	    类型：string，	                说明：出生日期
    ## 字段：CardNum，	        是否必选：是	    类型：string，	                说明：卡号
    ## 字段：NameChn             是否必选：是	    类型：string，	                说明：姓名
    ## 字段：NameEng，	        是否必选：是	    类型：string，	                说明：姓名拼音
    ## 字段：Sex，	            是否必选：是	    类型：string，	                说明：性别
    ## 字段：ValidDate，	        是否必选：是	    类型：string，	                说明：有效期限
    'TAIWAN_EXITENTRYPERMIT': 'https://aip.baidubce.com/rest/2.0/ocr/v1/taiwan_exitentrypermit',
    # 表格文字识别(异步接口)
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：long，	                说明：唯一的log id，用于问题定位
    ## 字段：result，	            是否必选：是	    类型：list，	                说明：返回的结果列表
    ## 字段：+request_id         是否必选：是	    类型：string，	                说明：该请求生成的request_id，后续使用该request_id获取识别结果
    'FORM_ORC_REQUEST': 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request',
    # 表格文字识别(异步接口), 获取请求结果
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：request_id，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：发送表格文字识别请求时返回的request id
    ## 参数：result_type，                        是否必选：False，         类型：string，    可选值范围：null，                  说明：期望获取结果的类型，取值为“excel”时返回xls文件的地址，取值为“json”时返回json格式的字符串,默认为”excel”
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：long，	                说明：唯一的log id，用于问题定位
    ## 字段：result，	            是否必选：是	    类型：object，	            说明：返回的结果列表
    ## 字段：+result_data，	    是否必选：是	    类型：string，	            说明：识别结果字符串，如果request_type是excel，则返回excel的文件下载地址，如果request_type是json，则返回json格式的字符串
    ## 字段：+percent，	        是否必选：是	    类型：int，	                说明：表格识别进度（百分比）
    ## 字段：+request_id         是否必选：是	    类型：string，	            说明：该图片对应请求的request_id
    ## 字段：+ret_code，	        是否必选：是	    类型：int，	                说明：识别状态，1：任务未开始，2：进行中,3:已完成
    ## 字段：+ret_msg，	        是否必选：是	    类型：string，	            说明：识别状态信息，任务未开始，进行中,已完成
    'FORM_ORC_GET_REQUEST_RESULT': 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result',
    # 表格文字识别(同步接口)
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，         类型：string，    可选值范围：null，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：long，	                说明：唯一的log id，用于问题定位
    ## 字段：forms_result_num，	是否必选：是	    类型：uint32，	                说明：识别结果元素个数
    ## 字段：forms_result        是否必选：是	    类型：object，	                说明：识别结果
    ## 字段：-body               是否必选：是	    类型：object，	                说明：表格主体区域
    ## 字段：-footer             是否必选：是	    类型：object，	                说明：表格尾部区域信息
    ## 字段：header              是否必选：是	    类型：object，	                说明：表格头部区域信息
    ## 字段：vertexes_location   是否必选：是	    类型：object，	                说明：表格边界顶点
    'FORM': 'https://aip.baidubce.com/rest/2.0/ocr/v1/form',
    # 通用票据识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，          类型：string，    可选值范围：null，               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：recognize_granularity，         是否必选：false，         类型：string，    可选值范围：big、small，         说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：probability，                   是否必选：false，         类型：string，    可选值范围：true、false，        说明：是否返回识别结果中每一行的置信度
    ## 参数：accuracy，                      是否必选：false，         类型：string，    可选值范围：normal,缺省，         说明：normal 使用快速服务;缺省或其它值使用高精度服务
    ## 参数：detect_direction，              是否必选：false，         类型：string，    可选值范围：true、false，         说明：是否检测图像朝向，默认不检测，即：false。可选值包括true - 检测朝向；false - 不检测朝向。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	            是否必选：是	    类型：uint64，	                说明：唯一的log id，用于问题定位
    ## 字段：words_result_num，	是否必选：是	    类型：uint32，	                说明：识别结果数，表示words_result的元素个数
    ## 字段：words_result，	    是否必选：是	    类型：array()，	                说明：定位和识别结果数组
    ## 字段：location，	        是否必选：是	    类型：object，	                说明：位置数组（坐标0点为左上角）
    ## 字段：left，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形的宽度
    ## 字段：height，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形的高度
    ## 字段：words，	            是否必选：是	    类型：string，	                说明：识别结果字符串
    ## 字段：chars，	            是否必选：否	    类型：array()，	                说明：单字符结果，recognize_granularity=small时存在
    ## 字段：location，	        是否必选：是	    类型：array()，	                说明：位置数组（坐标0点为左上角）
    ## 字段：left，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	            是否必选：是	    类型：uint32，	                说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	            是否必选：是	    类型：uint32，	                说明：表示定位定位位置的长方形的宽度
    ## 字段：height，	            是否必选：是	    类型：uint32，	                说明：表示位置的长方形的高度
    ## 字段：char，	            是否必选：是	    类型：long，	                    说明：单字符识别结果
    ## 字段：probability，	    是否必选：否		类型：object，	                说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'RECEIPT': 'https://aip.baidubce.com/rest/2.0/ocr/v1/receipt',
    # 增值税发票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，          类型：string，    可选值范围：null，               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：accuracy，                      是否必选：false，         类型：string，    可选值范围：normal、high，        说明：normal（默认配置）对应普通精度模型，识别速度较快，在四要素的准确率上和high模型保持一致，high对应高精度识别模型，相应的时延会增加，因为超时导致失败的情况也会增加（错误码282000）
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # 字段	是否必选	类型	说明
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	识别结果数组
    # InvoiceType	是	string	发票种类名称
    # InvoiceCode	是	uint32	发票代码
    # InvoiceNum	是	uint32	发票号码
    # InvoiceDate	是	uint32	开票日期
    # TotalAmount	是	uint32	合计金额
    # TotalTax	是	string	合计税额
    # AmountInFiguers	是	array()	价税合计(小写)
    # AmountInWords	是	object	价税合计(大写)
    # CheckCode	是	string	校验码
    # SellerName	是	uint32	销售方名称
    # SellerRegisterNum	是	uint32	销售方纳税人识别号
    # PurchaserName	是	uint32	购方名称
    # PurchaserRegisterNum	是	uint32	购方纳税人识别号
    # CommodityName	是	object[]	货物名称
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityType	是	object[]	规格型号
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityUnit	是	object[]	单位
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityNum	是	object[]	数量
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityPrice	是	object[]	单价
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityAmount	是	object[]	金额
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityTaxRate	是	object[]	税率
    # -row	是	uint32	行号
    # -word	是	string	内容
    # CommodityTax	是	object[]	税额
    # -row	是	uint32	行号
    # -word	是	string	内容
    'VAT_INVOICE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice',
    # 火车票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，          类型：string，    可选值范围：null，               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # 参数	类型	是否必须	说明
    # log_id	uint64	是	请求标识码，随机数，唯一。
    # ticket_num	string	是	车票号
    # starting_station	string	是	始发站
    # train_num	string	是	车次号
    # destination_station	string	是	到达站
    # date	string	是	出发日期
    # ticket_rates	string	是	车票金额
    # seat_category	string	是	席别
    # name	string	是	乘客姓名
    'TRAIN_TICKET': 'https://aip.baidubce.com/rest/2.0/ocr/v1/train_ticket',
    # 出租车票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，          类型：string，    可选值范围：null，               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # 参数	类型	是否必须	说明
    # log_id	uint64	是	请求标识码，随机数，唯一。
    # words_result_num	uint32	是
    # Date	string	是	日期
    # Fare	string	是	实付金额
    # InvoiceCode	string	是	发票代号
    # InvoiceNum	string	是	发票号码
    # TaxiNum	string	是	车牌号
    # Time	string	是	上下车时间
    'TAXI_RECEIPT': 'https://aip.baidubce.com/rest/2.0/ocr/v1/taxi_receipt',
    # 定额发票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，          类型：string，    可选值范围：null，               说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # 字段	是否必选	类型	说明
    # log_id	是	uint64	唯一的log id，用于问题定位
    # invoice_code	是	string	发票代码
    # invoice_number	是	string	发票号码
    # invoice_rate	是	string	金额
    'QUOTA_INVOICE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/quota_invoice',
    # 驾驶证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：detect_direction，              是否必选：false，          类型：string，    可选值范围：true、false，               说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:- true：检测朝向；- false：不检测朝向。
    ## 参数：unified_valid_period，          是否必选：false，          类型：bool，      可选值范围：true、false，               说明：true: 归一化格式输出；false 或无此参数按非归一化格式输出
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	识别结果数组
    # +words	否	string	识别结果字符串
    'DRIVING_LICENSE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license',
    # 行驶证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：detect_direction，              是否必选：false，          类型：string，    可选值范围：true、false，               说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:- true：检测朝向；- false：不检测朝向。
    ## 参数：accuracy，                      是否必选：false，          类型：bool，      可选值范围：normal，缺省，               说明：normal 使用快速服务，1200ms左右时延；缺省或其它值使用高精度服务，1600ms左右时延
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # 字段	必选	类型	说明
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	识别结果数组
    # +words	否	string	识别结果字符串
    'VEHICLE_LICENSE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license',
    # 车牌识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：multi_detect，                  是否必选：false，          类型：boolen，    可选值范围：true、false，               说明：是否检测多张车牌，默认为false，当置为true的时候可以对一张图片内的多张车牌进行识别
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	uint64	是	请求标识码，随机数，唯一。
    # Color	string	是	车牌颜色
    # number	string	是	车牌号码
    # probability	string	是	车牌中每个字符的置信度，区间为0-1
    # vertexes_location	string	是	返回文字外接多边形顶点位置
    'LICENSE_PLATE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate',
    # 机动车销售发票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # InvoiceNum	是	string	发票号码
    # 发票号码	是	string	定位和识别结果数组
    # PriceTaxLow	是	string	价税合计小写
    # PayerCode	是	string	纳税人识别号
    # InvoiceCode	是	string	发票代码
    # InvoiceDate	是	string	开票日期
    # EngineNum	是	string	发动机号码
    # ManuModel	是	string	厂商型号
    # Price	是	string	不含税价格
    # Saler	是	string	销售方
    # PriceTax	是	string	价税合计
    # Tax	是	string	税额
    # MachineCode	是	string	机器编码
    # VinNum	是	string	车架号
    'VEHICLE_INVOICE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_invoice',
    # 车辆合格证识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # InnerSize	是	string	货箱内部尺寸
    # VinNo	是	string	车架号
    # Power	是	string	功率
    # FuelType	是	string	燃油种类
    # EmissionStandard	是	string	排放标准
    # TyreNum	是	string	轮胎数
    # CertificationNo	是	string	合格证编号
    # EngineNo	是	string	发动机编号
    # ChassisType	是	string	底盘型号/底盘ID
    # CarName	是	string	车辆品牌/车辆名称
    # EngineType	是	string	发动机型号
    # AxleNum	是	string	轴数
    'VEHICLE_CERTIFICATE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_certificate',
    # 车辆VIN码识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：imgDirection	                    是否必选：否	            类型: string	    可选值范围：默认、setImgDirFlag	          说明：该参数决定模型是否自动纠正图像方向，默认不检测，当该参数=setImgDirFlag 时自动检测、纠正图像方向并识别
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # word	是	string	VIN码值
    'VIN_CODE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vin_code',
    # 二维码识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # codes_result_num	是	uint32	识别结果数，表示codes_result的元素个数
    # codes_result	是	array()	定位和识别结果数组
    # -type	是	string	识别码类型条码类型包括：9种条形码（UPC_A、UPC_E、EAN_13、EAN_8、CODE_39、CODE_93、CODE_128、ITF、CODABAR），4种二维码（QR_CODE、DATA_MATRIX、AZTEC、PDF_417）
    # -text	是	string
    'QRCODE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/qrcode',
    # 数字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：recognize_granularity	       是否必选：false	        类型：string      可选值范围：	big、small	             说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：detect_direction		           是否必选：FALSE             类型：string	 可选值范围：true、false	             说明：是否检测图像朝向，默认不检测，即：false。可选值包括true - 检测朝向；false - 不检测朝向。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	定位和识别结果数组
    # location	是	object	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位位置的长方形的宽度
    # height	是	uint32	表示定位位置的长方形的高度
    # words	是	string	识别结果字符串
    # chars	否	array()	单字符结果，recognize_granularity=small时存在
    # location	是	array()	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位定位位置的长方形的宽度
    # height	是	uint32	表示位置的长方形的高度
    # char	是	string	单字符识别结果
    'NUMBERS': 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers',
    # 彩票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## image	是	string	-	图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## recognize_granularity	false	string	big、small	是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	定位和识别结果数组
    # location	是	object	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位位置的长方形的宽度
    # height	是	uint32	表示定位位置的长方形的高度
    # words	是	string	识别结果字符串
    # chars	否	array()	单字符结果，recognize_granularity=small时存在
    # location	是	array()	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位定位位置的长方形的宽度
    # height	是	uint32	表示位置的长方形的高度
    # char	是	string	单字符识别结果
    'LOTTERY': 'https://aip.baidubce.com/rest/2.0/ocr/v1/lottery',
    # 保单识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    # image	是	string	-	图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # rkv_business	否	string	true/false	是否进行商业逻辑处理，rue：进行商业逻辑处理，false：不进行商业逻辑处理，默认true
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	object	定位和识别结果数组
    # BenPerLst	否	object	受益人信息
    # BenPerLst	否	string	受益人姓名
    # BenPerPro	否	string	受益比例
    # BenPerOrd	否	string	受益顺序
    # BenPerTyp	否	string	受益人类型
    # InsBilCom	否	string	公司名称
    # InsBilNo	否	string	保险单号码
    # InsBilTim	否	string	保单生效日期
    # InsCltGd1	否	string	投保人性别
    # InsCltNa1	否	string	投保人
    # InsIdcNb1	否	string	投保人证件号码
    # InsIdcTy1	否	string	投保人证件类型
    # InsPerLst	否	object	被保人信息
    # InsCltGd2	否	string	被保人性别
    # InsCltNa2	否	string	被保险人
    # InsBthDa2	否	string	被保险人出生日期
    # InsIdcNb2	否	string	被保险人证件号码
    # InsIdcTy2	否	string	被保险人证件类型
    # InsPrdList	否	object	保险信息
    # InsCovDur	否	string	保险期限
    # InsIcvAmt	否	string	基本保险金额
    # InsPayDur	否	string	交费期间
    # InsPayFeq	否	string	缴费频率
    # InsPerAmt	否	string	每期交费金额
    # InsPrdNam	否	string	产品名称
    'INSURANCE_DOCUMENTS': 'https://aip.baidubce.com/rest/2.0/ocr/v1/insurance_documents',
    # 税务局通用机打发票识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    # image	是	string	-	图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # location	否	string	true/false	是否输出位置信息，true：输出位置信息，false：不输出位置信息，默认false
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	object	定位和识别结果数组
    # CommodityName	否	string	商品名称
    # InvoiceCode	否	string	发票代码
    # InvoiceDate	否	string	发票日期
    # InvoiceNum	-	-	发票号码
    # InvoiceType	-	-	发票类型
    # TotalTax	-	-	合计金额
    'INVOICE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/invoice',
    # 行程单识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    # image	是	string	-	图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	object	定位和识别结果数组
    # name	否	string	姓名
    # starting_station	否	string	始发站
    # destination_station	否	string	目的站
    # flight	否	string	航班号
    # date	否	string	日期
    # ticket_rates	否	string	票价
    'AIR_TICKET': 'https://aip.baidubce.com/rest/2.0/ocr/v1/air_ticket',
}
