# Generated by Django 4.1 on 2022-09-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_aboutme_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
    ]
