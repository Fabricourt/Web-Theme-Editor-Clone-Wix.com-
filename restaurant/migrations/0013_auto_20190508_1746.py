# Generated by Django 2.2.1 on 2019-05-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_auto_20190508_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='restdb',
            name='Email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restdb',
            name='Your_Message',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
