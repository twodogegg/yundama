# -*- coding: utf-8 -*-
__author__ = 'twodogegg'
import hashlib
import time
import json
import requests
from yundama.Logger import Logger
import os
from datetime import datetime


class Yundama:
    __app_id = ''
    __app_key = ''
    __timestamp = ''

    def __init__(self, app_id, app_key):
        self.__app_id = app_id
        self.__app_key = app_key
        self.__timestamp = str(int(time.time()))

    """
    取得余额信息和返回信息
    返回示例：
    {'RetCode': '0', 'ErrMsg': 'succ', 'RequestId': '', 'RspData': {'cust_val': 820}}
    """

    def get_balance(self):
        url = 'http://pred.fateadm.com/api/custval'
        response = requests.post(url=url, data={
            'user_id': self.__app_id,
            'timestamp': self.__timestamp,
            'sign': self.__sign()
        }).json()
        return self.__handle_response(response)

    """
    直接取得余额的数值
    返回示例：
    820
    """

    def get_balance_result(self):
        result = self.get_balance()
        return result['RspData']['cust_val']

    """
    取得验证码识别结果和返回信息
    Content-type 请用application/x-www-form-urlencoded，暂时不支持application/json传输
    :img_data 图片的base_64数据
    : predict_type 验证码类型 http://docs.fateadm.com/web/#/1?page_id=36
    返回示例:
    {'RetCode': '0', 'ErrMsg': '', 'RequestId': '2020010110005008c25ef6000503c61a', 'RspData': {'result': '9unr'}}
    """

    def get_code(self, img_data, predict_type):
        url = 'http://pred.fateadm.com/api/capreg'
        response = requests.post(url=url, data={
            'user_id': self.__app_id,
            'timestamp': self.__timestamp,
            'sign': self.__sign(),
            'app_id': self.__app_key,
            'asign': self.__asign(),
            'predict_type': predict_type,
            "up_type": "mt"
        }, files={
            'img_data': ('img_data', img_data)
        }, headers={
            'User-Agent': 'Mozilla/5.0',
        }).json()
        return self.__handle_response(response)

    """
    直接取得验证码的识别结果
    返回示例：
    9unr
    """

    def get_code_result(self, img_data, predict_type):
        result = self.get_code(img_data, predict_type)
        return result['RspData']['result']

    """
    识别失败时进行退款，请勿滥用
    :request_id 识别时返回的 RequestId
    """

    def refund(self, request_id):
        url = 'http://pred.fateadm.com/api/capjust'
        response = requests.post(url=url, json={
            'user_id': self.__app_key,
            'timestamp': self.__timestamp,
            'sign': self.__sign(),
            'request_id': request_id
        }).json()
        return self.__handle_response(response)

    """
    充值操作
    :card_id 充值卡号
    :card_key 充值卡密
    """

    def recharge(self, card_id, card_key):
        url = 'http://pred.fateadm.com/api/charge'
        response = requests.post(url=url, json={
            'user_id': self.__app_key,
            'timestamp': self.__timestamp,
            'sign': self.__sign(),
            'csign': self.__csign(card_id, card_key),
            'card_id': card_id
        }).json()
        return self.__handle_response(response)

    def __sign(self):
        return self.__md5(self.__app_id + self.__timestamp + self.__md5(self.__timestamp + self.__app_key))

    def __asign(self):
        return self.__md5(self.__app_key + self.__timestamp + self.__md5(self.__timestamp + self.__app_id))

    def __csign(self, card_id, card_key):
        return self.__md5(self.__app_key + self.__timestamp + card_id + card_key)

    """
    对返回值进行处理
    """

    @staticmethod
    def __handle_response(response):

        if int(response['RetCode']) > 0:
            dir = os.path.abspath('../logs')
            filename = str(datetime.now().date()) + '-error'
            log = Logger(filename=filename, dir=dir)
            log.error(response)
            raise RuntimeError("错误码： %s，错误信息：%s" % (response['RetCode'], response['ErrMsg']))
        else:
            log = Logger(dir=os.path.abspath('../logs'))
            log.info(response)
            response['RspData'] = json.loads(response['RspData'])
            return response

    @staticmethod
    def __md5(value):
        md5 = hashlib.md5()
        md5.update(value.encode())
        return md5.hexdigest()
