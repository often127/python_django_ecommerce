# Generated by Django 3.2.7 on 2021-09-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='phone_number',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='merchantuser',
            name='phone_number',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='categories',
            name='url_slug',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='merchantuser',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='url_slug',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='url_slug',
            field=models.CharField(max_length=255),
        ),
    ]