# Generated by Django 4.2.7 on 2023-11-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=125)),
                ('l_name', models.CharField(default='', max_length=125)),
                ('cpf', models.CharField(max_length=11)),
                ('cep', models.CharField(default='', max_length=8)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
