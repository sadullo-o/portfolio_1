# Generated by Django 4.1 on 2022-09-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_myusers_about_myusers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='image',
            field=models.ImageField(default='blank-profile-picture-973460_1280.jpg', upload_to=''),
        ),
    ]
