# Generated by Django 4.0 on 2023-05-05 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=128, unique=True, verbose_name='Field Name')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=512, verbose_name='Project Title')),
                ('project_img', models.ImageField(upload_to='uploads/projects/', verbose_name='Project Image')),
                ('github_link', models.CharField(max_length=2048, unique=True, verbose_name='GitHub Link')),
                ('description', models.TextField(verbose_name='Description')),
                ('project_slug', models.SlugField(verbose_name='Project Slug')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=512, verbose_name='Last Name')),
                ('info', models.TextField(verbose_name='Information')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('phone', models.CharField(max_length=512, unique=True, verbose_name='Mobile Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('github_link', models.CharField(max_length=2048, unique=True, verbose_name='GitHub Link')),
                ('telegram', models.CharField(max_length=2048, unique=True, verbose_name='Telegram Link')),
                ('instagram', models.CharField(max_length=2048, unique=True, verbose_name='Instagram Link')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.field')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
