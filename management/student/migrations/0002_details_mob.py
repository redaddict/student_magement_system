# Generated by Django 4.2.6 on 2023-10-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='mob',
            field=models.IntegerField(null=True),
        ),
    ]
