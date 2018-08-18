# coding:utf-8
from django.db import models

class ContactUs(models.Model):
    wuqianzongbu = models.TextField(max_length = 10000,
            verbose_name = u"悟茜总部<html>")
    xiashugongsi = models.TextField(max_length = 10000,
            verbose_name = u"下属公司<html>")

    class Meta:
        verbose_name = u'联系我们'
        verbose_name_plural = u'联系我们'
