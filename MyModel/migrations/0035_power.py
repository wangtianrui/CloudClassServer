# Generated by Django 2.1.1 on 2019-07-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0034_coursemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('time', models.IntegerField()),
                ('course_id', models.CharField(max_length=20)),
            ],
        ),
    ]
