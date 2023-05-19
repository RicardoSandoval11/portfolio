# Generated by Django 4.2 on 2023-04-13 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_project_title', models.CharField(max_length=200, verbose_name='View project name')),
                ('view_project_description', models.TextField()),
                ('view_project_img', models.ImageField(upload_to='desc_imgs')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Description',
            },
        ),
    ]