# Generated by Django 2.1.1 on 2019-07-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0035_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('courseId', models.CharField(max_length=20)),
                ('studentId', models.CharField(max_length=20)),
            ],
        ),
    ]