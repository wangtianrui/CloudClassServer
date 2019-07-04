# Generated by Django 2.1.1 on 2019-07-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0033_auto_20190628_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('section', models.IntegerField()),
                ('week', models.IntegerField()),
                ('span', models.IntegerField()),
                ('user_id', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=40)),
                ('classroom_number', models.CharField(max_length=20)),
            ],
        ),
    ]
