# Generated by Django 2.1.1 on 2019-06-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyModel', '0025_mysource_source_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysource',
            name='uper_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
