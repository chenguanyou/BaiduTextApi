# BaiduTextApi
百度文字识别Api封装，在之前的基础上重写了下，更易于使用!

调用方式：
------
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 09:48
# @User    : zhunishengrikuaile
# @File    : test.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: 百度识图Api封装
from bin.AccessToken.AccessToken import AccessToken  # 测试获取AccessToken
from bin.GeneralBasic.GeneralBasic import GeneralBase  # 测试通用文字识别
from bin.AccurateBase.AccurateBase import AccurateBase  # 通用文字识别(高精度版)
from bin.General.General import General  # 通用文字识别（含位置信息版）
from bin.Accurate.Accurate import Accurate  # 通用文字识别（含位置高精度版）
from bin.GeneralEnhanced.GeneralEnhanced import GenneralEnhanced  # 通用文字识别（含生僻字版）
from bin.WebImage.WebImage import WebImage  # 网络图片文字识别
from bin.HandWriTing.HandwRiTing import HandwRiTing  # 手写文字识别
from bin.Idcard.Idcard import Idcard  # 身份证识别
from bin.BankCard.BankCard import BankCard  # 银行卡识别
from bin.BusinessLicense.BusinessLicense import BusinessLicense  # 营业执照识别
from bin.Passport.Passport import Passport  # 护照识别
from bin.BusunessCard.BusunessCard import BusunessCard  # 名片识别
from bin.HouseholdRegister.HouseholdRegister import HouseholdRegister  # 户口本识别
from bin.BirthCertificate.BirthCertificate import BirthCerTificate  # 出生医学证明识别
from bin.HkMacauExitentrpermit.HkMacauExitentrpermit import HkMavauExitentrpermit  # 港澳通行证识别
from bin.TaiwanExitentrupermit.TaiwanExitentrupermit import TaiwanExitentrupermit  # 台湾通行证识别
from bin.FormOrc.FormOrc import FormOrcRequest, FormOrcGetRequestResult  # 表格文字识别(异步接口)
from bin.Form.Form import Form  # 表格文字识别(同步接口)
from bin.Receipt.Receipt import Receipt  # 通用票据识别
from bin.VatInvouce.VatInvoice import VatInvoice  # 增值税发票识别
from bin.TrainTicket.TrainTicket import TrainTicket  # 火车票识别
from bin.TaxiReceipt.TaxiReceipt import TaxiReceipt  # 出租车票识别
from bin.QuotaInvoice.QuotaInvoice import QuotaInvoice  # 定额发票识别
from bin.DrivingLicense.DrivingLicense import DrivingLicense  # 驾驶证识别
from bin.VehicleLicense.VehicleLicense import VehicleLicense  # 行驶证识别
from bin.LicensePlate.LicensePlate import LicensePlate  # 车牌号识别
from bin.VehicleInvoice.VehicleInvoice import VehicleInvoice  # 机动车销售发票识别
from bin.VehicleCertificate.VehicleCertificate import VehicleCertificate  # 车辆合格证识别
from bin.VinCode.VinCode import VinCode  # 车辆VIN码识别
from bin.Qrcode.Qrcode import Qrcode  # 二维码识别
from bin.Numbers.Numbers import Numbers  # 数字识别
from bin.Lottery.Lottery import Lottery  # 彩票识别
from bin.InsuranceDocuments.InsuranceDocuments import InsuranceDocuments  # 保单识别
from bin.Invoice.Invoice import Invoice  # 税务局通用机打发票识别
from bin.AirTicket.AirTicket import AirTicket  # 行程单识别

if __name__ == '__main__':
    image = 'generalBasic.png'  # 普通图片
    IDCARD_IMAGE = ['IDCARD0.jpeg', 'IDCARD1.png']  # 身份证识别测试照片 0正面，1反面
    BANK_CARD_IMAGE = 'bankcard.jpeg'  # 银行卡
    BUSINESS_LICENSE = 'business_license.jpeg'  # 营业执照
    PASSPORT_IMAGES = 'passport.jpeg'  # 护照识别
    EX = 'ex.jpeg'  # 表格
    ZZS = 'ZZS.jpg'  # 增值税发票
    HCP = 'HCP.jpg'  # 火车票
    CZC = 'CZC.jpg'  # 出驻车票
    DEFP = 'DEFP.jpeg'  # 定额发票
    JSZ = 'JSZ.jpg'  # 驾驶证
    XSZ = 'XSZ.jpg'  # 行驶证识别
    CPH = 'CPH.jpg'  # 车牌号
    JDCXSFP = 'JDCXSFP.png'  # 机动车销售发票
    NUMBERS = 'NUMBERS.jpg'  # 数字
    url = 'https://user-gold-cdn.xitu.io/2018/6/27/16441ddfa026968b?w=513&h=389&f=png&s=2155'  # 网络图片

    # 测试获取AccessToken
    testAccessToken = AccessToken()
    print('Access_token:', testAccessToken.getToken())

    # 测试通用文字识别
    testGeneralBasic = GeneralBase(image=image)
    print('通用文字识别：', testGeneralBasic.postGeneralBase())

    # 通用文字识别(高精度版)
    testAccurateBase = AccurateBase(image=image)
    print('通用文字识别(高精度版):', testAccurateBase.postAccurateBase())

    # 通用文字识别（含位置信息版）
    testGeneral = General(image=image)
    print('通用文字识别（含位置信息版）:', testGeneral.postGeneral())

    # 通用文字识别（含位置高精度版）
    testAccurate = Accurate(image=image)
    print('通用文字识别（含位置高精度版）:', testAccurate.postAccurate())

    # 通用文字识别（含生僻字版）
    # https://cloud.baidu.com/doc/OCR/OCR-API.html#.CC.97.73.06.FD.A1.D8.DE.4F.1F.5E.CF.E4.1A.E6.B9
    testGeneralEnhanced = GenneralEnhanced(image=image)
    print('通用文字识别（含生僻字版）:', testGeneralEnhanced.postGenneralEnhanced())

    # 网络图片文字识别
    testWebImage = WebImage(image=image)
    print('网络图片文字识别: ', testWebImage.postWebImage())

    # 测试手写文字识别
    testHandTing = HandwRiTing(image=image)
    print('手写文字识别: ', testHandTing.postHandwRiTing())

    # 身份证识别, 正面
    # front：身份证含照片的一面；back：身份证带国徽的一面
    testIdcard = Idcard(image=IDCARD_IMAGE[0], id_card_side='front')
    print('身份证识别正面：', testIdcard.postIdcard())

    # 身份证识别, 反面
    # front：身份证含照片的一面；back：身份证带国徽的一面
    testIdcard1 = Idcard(image=IDCARD_IMAGE[1], id_card_side='back')
    print('身份证识别反面：', testIdcard1.postIdcard())

    # 银行卡识别
    testBankCard = BankCard(image=BANK_CARD_IMAGE)
    print('银行卡识别：', testBankCard.postBankCard())

    # 营业执照识别
    testBusinessLicense = BusinessLicense(image=BUSINESS_LICENSE)
    print('营业执照识别：', testBusinessLicense.postBusinessLicense())

    # 护照识别, 这个需要权限
    testPassport = Passport(image=PASSPORT_IMAGES)
    print('护照识别：', testPassport.postPassport())

    # 名片识别，需要权限
    testBusunessVard = BusunessCard(image=image)
    print('名片识别：', testBusunessVard.postBusunessCard())

    # 户口本识别， 需要权限
    testHouseholdRegister = HouseholdRegister(image=image)
    print('户口本识别: ', testHouseholdRegister.postHouseholdRegiater())

    # 出生医学证明识别，需要权限
    testBirthCerTificate = BirthCerTificate(image=image)
    print('出生医学证明识别: ', testBirthCerTificate.postBirthCerTificate())

    # 港澳通行证识别，需要权限
    testHkMavauExitentrpermit = HkMavauExitentrpermit(image=image)
    print('港澳通行证识别: ', testHkMavauExitentrpermit.postHkMavauExitentrpermit())

    # 台湾通行证识别，需要权限
    testTaiwanExitentrupermit = TaiwanExitentrupermit(image=image)
    print('台湾通行证识别：', testTaiwanExitentrupermit.postTaiwanExitentrupermit())

    # 表格文字识别(异步接口)，这里返回图片id, 正确json格式数据，{'result': [{'request_id': '14348843_892436'}], 'log_id': 15504569495689228}
    testFormOrcRequest = FormOrcRequest(image=EX)
    request_id = testFormOrcRequest.postFormOrcRequest()['result'][0]['request_id']
    testFormOrcGetRequestResult = FormOrcGetRequestResult(request_id='14348843_892480').postFormOrcGetRequestResult()
    print('表格文字识别异步接口：', request_id, testFormOrcGetRequestResult)

    # 表单文字识别，同步接口, 需要权限
    testForm = Form(image=EX)
    print('表单文字识别同步接口：', testForm.postForm())

    # 通用票据识别
    testReceipt = Receipt(image=EX)
    print('通用票据识别：', testReceipt.postReceipt())

    # 测试增值税发票识别
    testVatInvoice = VatInvoice(image=ZZS, accuracy='high')
    print('增值税发票识别：', testVatInvoice.postVatInvoice())

    # 火车票识别
    testTrainTicket = TrainTicket(image=HCP)
    print('火车票识别：', testTrainTicket.postTrainTicket())

    # 出租车票识别
    testTaxiReceipt = TaxiReceipt(image=CZC)
    print('出租车票识别：', testTaxiReceipt.postTaxiReceipt())

    # 定额发票识别,需要权限
    testQuotaInvoice = QuotaInvoice(image=DEFP)
    print('定额发票识别：', testQuotaInvoice.postQuotaInvoice())

    # 驾驶证识别
    testDrivingLicense = DrivingLicense(image=JSZ)
    print('驾驶证识别：', testDrivingLicense.postDrivingLicense())

    # 行驶证识别
    testVehicleLicense = VehicleLicense(image=XSZ)
    print('行驶证识别：', testVehicleLicense.postVehicleLicense())

    # 车牌号识别
    testLicensePlate = LicensePlate(image=CPH)
    print('车牌号识别：', testLicensePlate.postLicensePlate())

    # 机动车销售发票识别，需要权限
    testVehicleInvoice = VehicleInvoice(image=JDCXSFP)
    print('机动车销售发票识别：', testVehicleInvoice.postVehicleInvoice())

    # 车辆合格证识别，需要权限
    testVehicleCertificate = VehicleCertificate(image=JDCXSFP)
    print('车辆合格证识别: ', testVehicleCertificate.postVehicleCertificate())

    # 车辆Vin号码识别，需要权限
    testVinCode = VinCode(image=JDCXSFP)
    print('车辆Vin号码识别: ', testVinCode.postVinCode())

    # 二维码识别，需要权限
    testQrcode = Qrcode(image=JDCXSFP)
    print('二维码识别：', testQrcode.postQrcode())

    # 数字识别
    testNumbers = Numbers(image=NUMBERS)
    print('数字识别：', testNumbers.postNumbers())

    #     彩票识别，需要权限
    testLottery = Lottery(image=image)
    print('彩票识别：', testLottery.postLottery())

    # 保单识别,需要权限
    testInsuranceDocuments = InsuranceDocuments(image=image)
    print('保单识别：', testInsuranceDocuments.postInsuranceDocuments())

    # 税务局通用机打发票识别, 需要权限
    testInvoice = Invoice(image=image)
    print('税务局通用机打发票识别: ', testInvoice.postInvoice())

    # 行程单识别, 需要权限
    testAirTicket = AirTicket(image=image)
    print('行程单识别：', testAirTicket.postAirTicket())

```
