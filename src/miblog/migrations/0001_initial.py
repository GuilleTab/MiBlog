# Generated by Django 4.0.6 on 2022-08-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mi_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.CharField(max_length=6000)),
                ('logo', models.FileField(upload_to='')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
