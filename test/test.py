# -*- coding: utf-8 -*-
__author__ = 'twodogegg'
from yundama.Yundama import Yundama


def main():
    yundama = Yundama(app_id="你的PD账号", app_key="你的PD秘钥")
    balance = yundama.get_balance_result()
    print(balance)
    img = open('../data/image.png', 'rb')
    result = yundama.get_code_result(img.read(), '30400')
    print(result)

    # result = yundama.refund('订单id')
    # result = yundama.recharge('充值卡号', '充值卡密')


if __name__ == '__main__':
    main()
