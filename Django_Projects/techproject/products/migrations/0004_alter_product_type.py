# Generated by Django 3.2 on 2021-04-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
