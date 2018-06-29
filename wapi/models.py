from django.db import models


class ScggjyList(models.Model):
    title = models.CharField(max_length=255)
    pubData = models.CharField(max_length=255)
    detailLink = models.CharField(max_length=255)
    detailTitle = models.CharField(max_length=255)

    class Meta:
        db_table = 'wdjango_scggjy_list'
