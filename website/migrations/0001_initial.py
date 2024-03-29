# Generated by Django 4.2.2 on 2023-06-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
            ],
        ),
    ]
