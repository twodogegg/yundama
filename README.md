## 前言
本来是想找一个python 识别二维码的。可是网上网上找到的教程都是教人怎么自己写一个用例去请求打码请求，或是自己找第三方库实现。
显然这都不是我想要的。我想要的就是拿来即用。

上诉两种方案其一需要自己写，代码复用率不高，或是直接从平台复制用例对代码侵入比较大。其二的识别率不高。

## 解决痛点

1. `pip` 直接安装无需关注实现细节
2. 保持更新。稳定可用
3. 识别率搞
4. 识别结果记录log 识别失败可退款

## todo

1. 接入其他打码平台

## 斐斐云打码

> 使用 斐斐打码 对验证码进行打码。一次封装简单使用

## 测试账号

PD账号:119208

PD秘钥:gfPmvlxPWdGEplGZtr3aIuaWP1/fyZW3


[打码平台地址](http://www.fateadm.com/)

## 如何使用

[官方文档地址](http://docs.fateadm.com/web/#/1?page_id=1)

测试用例 `test/test.py`

### 引入

```
pip install yundama
```

### 实例化
```
from yundama.Yundama import Yundama
yundama = Yundama(app_id="你的pd_id", app_key="你的pd_key")
```

### 查询余额

```
yundama.get_balance()
```

### 提交需要验证的图片

[类型说明](http://docs.fateadm.com/web/#/1?page_id=36)
```
img = open('../data/image.png', 'rb')
yundama.get_code_result(img.read(), '验证码类型')
```
### 退款

```
yundama.refund('订单id')
```
### 充值

```
yundama.recharge('充值卡号', '充值卡密')
```