# Generated by Django 4.1.4 on 2022-12-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelapp', '0003_alter_image_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
