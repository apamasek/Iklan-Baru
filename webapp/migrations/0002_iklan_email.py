# Generated by Django 3.0.6 on 2020-05-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iklan',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
