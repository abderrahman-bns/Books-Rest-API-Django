# Generated by Django 3.2.6 on 2021-08-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
