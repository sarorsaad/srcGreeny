# Generated by Django 4.1.1 on 2022-09-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('MRN', models.IntegerField()),
                ('Nationality', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=30)),
            ],
        ),
    ]
