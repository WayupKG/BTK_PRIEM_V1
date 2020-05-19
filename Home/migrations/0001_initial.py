# Generated by Django 2.2.8 on 2020-05-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Называние')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='Specialty/', verbose_name='Изображения')),
                ('publish', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ('-publish',),
            },
        ),
    ]
