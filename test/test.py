# -*- coding: utf-8 -*-
from datetime import datetime

__author__ = 'twodogegg'
from yundama.Yundama import Yundama

def main():

    yundama = Yundama(app_id="119208", app_key="gfPmvlxPWdGEplGZtr3aIuaWP1/fyZW3")
    balance = yundama.get_balance_result()
    print(balance)
    # img = open('../data/5682.jpeg', 'rb')
    img = open('../data/image.png', 'rb')
    result = yundama.get_code_result(img.read(), '30400')
    print(result)

    # result = yundama.refund('订单id')
    # result = yundama.recharge('充值卡号', '充值卡密')


if __name__ == '__main__':
    main()
