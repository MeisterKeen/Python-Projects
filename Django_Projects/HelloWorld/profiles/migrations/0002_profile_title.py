# Generated by Django 3.2 on 2021-04-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.'), ('Dr.', 'Dr.')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
