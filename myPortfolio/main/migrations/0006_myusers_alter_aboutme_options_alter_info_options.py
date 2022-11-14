# Generated by Django 4.1 on 2022-09-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone_number', models.CharField(default='', max_length=100, verbose_name='Phone Number')),
                ('full_name', models.CharField(default='', max_length=100, verbose_name='Full Name')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'My Users',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'xodim', 'verbose_name_plural': 'Xodimlar'},
        ),
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Xabar', 'verbose_name_plural': 'Xabarlar'},
        ),
    ]
