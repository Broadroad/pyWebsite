# coding:utf-8
from django.db import models

class AboutWuqian(models.Model):
    wuqiangaishu = models.TextField(verbose_name = u"悟茜概述<html>",
            max_length = 10000)
    wuqianzhanlve = models.TextField(verbose_name = u"悟茜战略<html>",
            max_length = 10000)
    hexinyoushi = models.TextField(verbose_name = u"核心优势<html>",
            max_length = 10000)
    fazhanlicheng = models.TextField(verbose_name = u"发展历程<html>",
            max_length = 10000)

    class Meta:
        verbose_name = u'关于悟茜'
        verbose_name_plural = u'关于悟茜'

