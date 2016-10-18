# django-wechat
微信公众号 django 开发库

Quick start
-----------

1. 添加 "djwechat" 到 INSTALLED_APPS中

    INSTALLED_APPS = (
        ...
        'djwechat',
    )

2. 运行 `python manage.py migrate`，以创建 django-wechat models.

3. 在admin后台，添加账号认证信息 和 JsApiList

1）账号认证信息的值为：

    {
      "WEIXIN_TOKEN": "6G9IH7EF4D83C5AB",
      "WEIXIN_APP_ID": "wx67fb1f4877bfd511",
      "WEIXIN_APP_SECRET": "646332665dcd63f9e8b83a474f2dbe38",
      "WEIXIN_ENCODING_AES_KEY": "ZvhDvkQ8QpRUvNZUQgDRvrU3ICQEBVEdLvEsmsXTscA"
    }

2）已申请的JsApiList权限，以空格隔开，如下所示：

    scanQRCode getLocation getNetworkType onMenuShareTimeline onMenuShareAppMessage onMenuShareQQ onMenuShareWeibo chooseWXPay
   
4. 在 `django` 中使用

    from djwechat.util import get_wechat
    wechat = get_wechat()
    ....

djwechat会自动在数据库中保存和更新 access_token、jsapi_ticket, 用户只需负责调用就行。