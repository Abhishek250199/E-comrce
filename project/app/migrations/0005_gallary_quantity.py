# Generated by Django 4.2.4 on 2023-09-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gallary_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallary',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
    ]