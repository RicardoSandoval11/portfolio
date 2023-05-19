# Generated by Django 4.2 on 2023-04-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('role', models.CharField(max_length=200, verbose_name='role')),
                ('profile_img', models.ImageField(upload_to='home', verbose_name='Image')),
                ('presentation', models.TextField()),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home',
            },
        ),
    ]
