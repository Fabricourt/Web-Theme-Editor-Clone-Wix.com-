# Generated by Django 2.2.1 on 2019-05-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restdb',
            name='brandimg',
            field=models.ImageField(blank=True, default='/static/img/logo.png', null=True, upload_to='images/'),
        ),
    ]
