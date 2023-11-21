# Generated by Django 4.2.7 on 2023-11-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Papel', 'Papel'), ('Plástico', 'Plástico'), ('Vidro', 'Vidro'), ('Metal', 'Metal'), ('Orgânico', 'Orgânico')], max_length=13)),
                ('ecopoint', models.CharField(max_length=5)),
            ],
        ),
    ]