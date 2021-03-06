# Generated by Django 3.2.5 on 2021-08-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('slides_url', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
