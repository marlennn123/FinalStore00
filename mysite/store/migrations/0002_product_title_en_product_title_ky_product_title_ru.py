# Generated by Django 5.0.6 on 2024-07-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]