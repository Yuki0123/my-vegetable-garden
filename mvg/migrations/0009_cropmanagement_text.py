# Generated by Django 3.0.4 on 2021-07-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvg', '0008_auto_20210705_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmanagement',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
    ]
