# Generated by Django 3.0.4 on 2020-03-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.FileField(null=True, upload_to='groceris/'),
        ),
    ]
