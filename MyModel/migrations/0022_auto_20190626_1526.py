# Generated by Django 2.1.1 on 2019-06-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0021_auto_20190626_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysource',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
