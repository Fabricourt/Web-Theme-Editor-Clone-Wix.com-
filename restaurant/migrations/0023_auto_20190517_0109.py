# Generated by Django 2.2.1 on 2019-05-16 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_restdbcontact_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restdb',
            name='spldish1img',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish1muted',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish1name',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish1price',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish2img',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish2muted',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish2name',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish2price',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish3img',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish3muted',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish3name',
        ),
        migrations.RemoveField(
            model_name='restdb',
            name='spldish3price',
        ),
    ]