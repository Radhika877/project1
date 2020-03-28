# Generated by Django 3.0.2 on 2020-03-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity_periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'activity_periods',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]