# coding = utf-8
from django.db import models


# 商品模型类
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=50)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=20, default='')
    uaddress = models.CharField(max_length=100, default='')
    upostcode = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')

    # default,blank是python层面的约束，不影响数据库表结构，不需要重新迁移

    class Meta:
        db_table = 'wdjango_user'
