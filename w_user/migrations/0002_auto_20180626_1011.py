# Generated by Django 2.0.6 on 2018-06-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upostcode',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20),
        ),
    ]
