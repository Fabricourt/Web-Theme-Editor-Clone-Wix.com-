# Generated by Django 2.2.1 on 2019-05-08 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_restdbcontact_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restdbcontact',
            name='theme',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='restaurant.RestDb'),
        ),
    ]
