# Generated by Django 3.2.8 on 2022-09-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img_course',
            field=models.ImageField(default='', upload_to='Course'),
        ),
    ]
