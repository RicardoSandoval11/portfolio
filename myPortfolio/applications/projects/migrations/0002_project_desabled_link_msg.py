# Generated by Django 4.2 on 2023-04-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desabled_link_msg',
            field=models.TextField(blank=True),
        ),
    ]
