# Generated by Django 2.0.6 on 2018-07-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapi', '0003_auto_20180629_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZakerNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ztitle', models.CharField(blank=True, db_column='zTitle', max_length=255, null=True, unique=True)),
                ('zsubtitle', models.CharField(blank=True, db_column='zSubtitle', max_length=255, null=True)),
                ('ssubimagelink', models.CharField(blank=True, db_column='sSubImageLink', max_length=255, null=True)),
                ('zdetaillink', models.CharField(blank=True, db_column='zDetailLink', max_length=255, null=True)),
                ('ztype', models.CharField(blank=True, db_column='zType', max_length=20, null=True)),
            ],
            options={
                'db_table': 'zaker_news',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='scggjylist',
            options={'managed': False},
        ),
    ]
