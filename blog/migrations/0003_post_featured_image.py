# Generated by Django 4.1.2 on 2022-10-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_timestamp_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, default='wood.png', null=True, upload_to=''),
        ),
    ]