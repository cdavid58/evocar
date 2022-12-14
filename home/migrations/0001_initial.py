# Generated by Django 3.2.8 on 2022-09-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_slogan', models.CharField(max_length=150)),
                ('company_logo', models.ImageField(upload_to='Logo')),
                ('text1_banner', models.CharField(max_length=250)),
                ('text2_banner', models.CharField(max_length=200)),
            ],
        ),
    ]
