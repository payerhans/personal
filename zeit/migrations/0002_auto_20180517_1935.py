# Generated by Django 2.0.5 on 2018-05-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='title_past',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='title_pre',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
