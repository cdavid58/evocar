# Generated by Django 3.2.8 on 2022-09-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_information_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='title_about',
            field=models.CharField(default='', max_length=100),
        ),
    ]
