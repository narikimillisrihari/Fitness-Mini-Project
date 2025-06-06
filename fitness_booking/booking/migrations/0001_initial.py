# Generated by Django 3.2.25 on 2025-06-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('instructor', models.CharField(max_length=250)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('available_slots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=250)),
                ('client_email', models.EmailField(max_length=254)),
                ('fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.fitness')),
            ],
        ),
    ]
