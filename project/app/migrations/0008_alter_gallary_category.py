# Generated by Django 4.2.4 on 2023-09-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_gallary_category_alter_gallary_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='Category',
            field=models.CharField(choices=[(1, 'smartwatch'), (2, 'dailwatch')], max_length=50, null=True),
        ),
    ]
