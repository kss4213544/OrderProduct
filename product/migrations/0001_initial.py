# Generated by Django 3.1.7 on 2021-06-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=40)),
                ('Product_price', models.CharField(max_length=40)),
                ('Category', models.CharField(max_length=40)),
            ],
        ),
    ]
