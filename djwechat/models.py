# -*- coding: utf-8 -*-
from django.db import models


class Config(models.Model):
    KIND_AUTH = 0
    KIND_JS_API_LIST = 1
    KIND_TOKEN = 2
    KIND_TICKET = 3
    KIND_CHOICES = (
        (KIND_AUTH, '账号认证信息'),
        (KIND_JS_API_LIST, 'JsApiList'),
        (KIND_TOKEN, 'token'),
        (KIND_TICKET, 'ticket')
    )
    kind = models.IntegerField(choices=KIND_CHOICES, verbose_name='类型')
    value = models.TextField(default='', verbose_name='值')

    def __unicode__(self):
        return '%s' % self.kind


