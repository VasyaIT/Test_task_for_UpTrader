# Generated by Django 4.2 on 2023-04-26 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the name of menu', max_length=255, unique=True, verbose_name='menu title')),
                ('slug', models.SlugField(help_text='URL', max_length=255, verbose_name='menu slug')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the name of Subject', max_length=255, verbose_name='subject title')),
                ('slug', models.SlugField(help_text='URL', max_length=255, verbose_name='subject slug')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.subject')),
            ],
            options={
                'verbose_name': 'Menu subject',
                'verbose_name_plural': 'Menu subjects',
            },
        ),
    ]
