# Generated by Django 2.0.2 on 2020-05-19 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('prof', models.TextField()),
                ('course', models.TextField()),
                ('school', models.TextField()),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
            ],
        ),
    ]
