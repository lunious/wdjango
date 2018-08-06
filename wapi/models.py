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

class ZakerNewsTab(models.Model):
    code = models.IntegerField(blank=True, null=True)
    tabName = models.CharField(db_column='tabName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zaker_news_tab'


class BxtZbgg(models.Model):
    area = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    ywtype = models.CharField(db_column='ywType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    xxtype = models.CharField(db_column='xxType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=40, blank=True, null=True)
    ly = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    pubdata = models.CharField(db_column='pubData', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deaddata = models.CharField(db_column='deadData', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=20, blank=True, null=True)
    itemnum = models.CharField(db_column='itemNum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detailurl = models.CharField(db_column='detailUrl', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bxt_zbgg'



