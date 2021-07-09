# Generated by Django 3.0.4 on 2021-07-04 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvg', '0005_auto_20210701_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growingcrop',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mvg.Area', verbose_name='栽培エリア'),
        ),
        migrations.AlterField(
            model_name='growingcrop',
            name='management_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mvg.ManagementGroup', verbose_name='管理グループ'),
        ),
        migrations.AlterField(
            model_name='growingcrop',
            name='variety',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mvg.Varietie', verbose_name='品種'),
        ),
    ]
