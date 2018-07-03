from django.db import models


class ScggjyList(models.Model):
    title = models.CharField(max_length=255)
    pubData = models.CharField(db_column='pubData', max_length=255)
    detailLink = models.CharField(db_column='detailLink', max_length=255)
    detailTitle = models.CharField(db_column='detailTitle', max_length=255)

    class Meta:
        managed = False
        db_table = 'scggjy_list'


class ZakerNews(models.Model):
    zTitle = models.CharField(db_column='zTitle', unique=True, max_length=255, blank=True, null=True)
    zSubtitle = models.CharField(db_column='zSubtitle', max_length=255, blank=True, null=True)
    sSubImageLink = models.CharField(db_column='sSubImageLink', max_length=255, blank=True, null=True)
    zDetailLink = models.CharField(db_column='zDetailLink', max_length=255, blank=True, null=True)
    zType = models.CharField(db_column='zType', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zaker_news'
