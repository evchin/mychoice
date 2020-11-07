# Generated by Django 3.1.2 on 2020-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20201101_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='elections',
        ),
        migrations.AddField(
            model_name='candidate',
            name='positions',
            field=models.ManyToManyField(to='votes.Position'),
        ),
    ]
