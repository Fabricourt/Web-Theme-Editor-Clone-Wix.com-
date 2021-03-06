# Generated by Django 2.2.1 on 2019-05-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='About_Us',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Banner_Heading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Banner_Text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Brand_Logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Our_Services',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
