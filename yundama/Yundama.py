# -*- coding: utf-8 -*-
__author__ = 'twodogegg'
import hashlib
import time
import json
import requests
from yundama.Logger import Log


class Yundama:
    app_id = ''
    app_key = ''

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.timestamp = str(int(time.time()))

    """
    取得余额信息
    """

    def get_balance(self):
        url = 'http://pred.fateadm.com/api/custval'
        response = requests.post(url=url, data={
            'user_id': self.app_id,
            'timestamp': self.timestamp,
            'sign': self.sign()
        }).json()
        return self.handle_response(response)

    """
    取得验证码识别结果
    Content-type 请用application/x-www-form-urlencoded，暂时不支持application/json传输
    :img_data 图片的base_64数据
    : predict_type 验证码类型 http://docs.fateadm.com/web/#/1?page_id=36 
    """

    def get_code_result(self, img_data, predict_type):
        url = 'http://pred.fateadm.com/api/capreg'
        response = requests.post(url=url, data={
            'user_id': self.app_id,
            'timestamp': self.timestamp,
            'sign': self.sign(),
            'app_id': self.app_key,
            'asign': self.asign(),
            'predict_type': predict_type,
            "up_type": "mt"
        }, files={
            'img_data': ('img_data', img_data)
        }, headers={
            'User-Agent': 'Mozilla/5.0',
        }).json()
        return response

    """
    识别失败时进行退款，请勿滥用
    :request_id 识别时返回的 RequestId
    """

    def refund(self, request_id):
        url = 'http://pred.fateadm.com/api/capjust'
        response = requests.post(url=url, json={
            'user_id': self.app_key,
            'timestamp': self.timestamp,
            'sign': self.sign(),
            'request_id': request_id
        }).json()
        return self.handle_response(response)

    """
    充值操作
    :card_id 充值卡号
    :card_key 充值卡密
    """

    def recharge(self, card_id, card_key):
        url = 'http://pred.fateadm.com/api/charge'
        response = requests.post(url=url, json={
            'user_id': self.app_key,
            'timestamp': self.timestamp,
            'sign': self.sign(),
            'csign': self.csign(card_id, card_key),
            'card_id': card_id
        }).json()
        return self.handle_response(response)

    def sign(self):
        return self.md5(self.app_id + self.timestamp + self.md5(self.timestamp + self.app_key))

    def asign(self):
        return self.md5(self.app_key + self.timestamp + self.md5(self.timestamp + self.app_id))

    def csign(self, card_id, card_key):
        return self.md5(self.app_key + self.timestamp + card_id + card_key)

    """
    对返回值进行处理
    """

    @staticmethod
    def handle_response(response):
        if int(response['RetCode']) > 0:
            Log("error :" + response['ErrMsg'])
            raise RuntimeError("错误码： %s，错误信息：%s" % (response['RetCode'], response['ErrMsg']))
        else:
            response['RspData'] = json.loads(response['RspData'])
            return response

    @staticmethod
    def md5(value):
        md5 = hashlib.md5()
        md5.update(value.encode())
        return md5.hexdigest()
