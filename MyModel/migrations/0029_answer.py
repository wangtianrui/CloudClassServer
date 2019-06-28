# Generated by Django 2.1.1 on 2019-06-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0028_auto_20190627_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to='media/answers')),
                ('uper_id', models.CharField(max_length=20)),
                ('up_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]