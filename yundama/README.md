## 斐斐云打码

使用 斐斐打码 对验证码进行打码。一次封装简单使用

[打码平台地址](http://www.fateadm.com/)

## 如何使用

[官方文档地址](http://docs.fateadm.com/web/#/1?page_id=1)

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