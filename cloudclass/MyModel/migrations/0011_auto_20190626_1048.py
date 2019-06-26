# Generated by Django 2.1.1 on 2019-06-26 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0010_auto_20190625_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='avatar',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='span',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='week',
            field=models.IntegerField(),
        ),
    ]
