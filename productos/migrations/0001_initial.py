# Generated by Django 4.1.1 on 2023-03-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('marca', models.TextField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
