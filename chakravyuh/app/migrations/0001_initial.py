# Generated by Django 4.0.4 on 2023-03-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corridor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
