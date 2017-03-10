# -*- coding: utf-8 -*-
from urllib import unquote
from wechat_sdk import WechatBasic
from .models import Config
import json


def get_access_token(appid):
    def _wrapper():
        try:
            obj = Config.objects.get(appid=appid, kind=Config.KIND_TOKEN)
            value = json.loads(obj.value)
            return value.get("access_token"), value.get("access_token_expires_at")
        except Config.DoesNotExist:
            return None, None
    return _wrapper


def set_access_token(appid):
    def _wrapper(access_token, access_token_expires_at):
        value = json.dumps({
            "access_token": access_token,
            "access_token_expires_at": access_token_expires_at
        })
        Config.objects.update_or_create(appid=appid, kind=Config.KIND_TOKEN, defaults={
            "value": value
        })
    return _wrapper


def get_jsapi_ticket(appid):
    def _wrapper():
        try:
            obj = Config.objects.get(appid=appid, kind=Config.KIND_TICKET)
            value = json.loads(obj.value)
            return value.get("jsapi_ticket"), value.get("jsapi_ticket_expires_at")
        except Config.DoesNotExist:
            return None, None
    return _wrapper


def set_jsapi_ticket(appid):
    def _wrapper(jsapi_ticket, jsapi_ticket_expires_at):
        value = json.dumps({
            "jsapi_ticket": jsapi_ticket,
            "jsapi_ticket_expires_at": jsapi_ticket_expires_at
        })
        Config.objects.update_or_create(appid=appid, kind=Config.KIND_TICKET, defaults={
            "value": value
        })
    return _wrapper


def get_wxjs_config(url, wx_tool):
    js_api_list = []
    try:
        obj = Config.objects.get(kind=Config.KIND_JS_API_LIST)
        value = json.loads(obj.value)
        js_api_list = value.split()
    except Config.DoesNotExist:
        pass

    url = unquote(url)
    param = {
        "debug": False,
        "jsApiList": js_api_list,
        "url": url
    }
    config = wx_tool.get_js_config(param)
    return config


Wechat = {}


def get_wechat(appid):
    global Wechat
    if not Wechat.get(appid):
        auth = None
        try:
            obj = Config.objects.get(appid=appid, kind=Config.KIND_AUTH)
            auth = json.loads(obj.value)
        except Config.DoesNotExist:
            pass
        else:
            # 实例化 wechat
            Wechat[appid] = WechatBasic(
                token=auth.get("WEIXIN_TOKEN"),
                appid=auth.get("WEIXIN_APP_ID"),
                appsecret=auth.get("WEIXIN_APP_SECRET"),
                partnerid=auth.get("WEIXIN_MCH_ID"),
                partnerkey=auth.get("WEIXIN_PARTNER_KEY"),
                notify_url=auth.get("WEIXIN_NOTIFY_URL"),
                get_access_token=get_access_token(appid),
                set_access_token=set_access_token(appid),
                get_jsapi_ticket=get_jsapi_ticket(appid),
                set_jsapi_ticket=set_jsapi_ticket(appid)
            )
    return Wechat[appid]

