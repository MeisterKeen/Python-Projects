# Generated by Django 3.2 on 2021-04-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Ms.', 'Ms.')], max_length=50),
        ),
    ]