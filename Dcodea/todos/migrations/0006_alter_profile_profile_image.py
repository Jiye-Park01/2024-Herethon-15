# Generated by Django 5.0.6 on 2024-07-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/default.svg', upload_to='profile_images/'),
        ),
    ]
