# Generated by Django 2.1.1 on 2019-06-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0023_auto_20190626_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='span',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='week',
            field=models.IntegerField(null=True),
        ),
    ]