# Generated by Django 4.2.4 on 2023-09-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_gallary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='Gender',
            field=models.CharField(choices=[(1, 'male'), (2, 'female'), (3, 'unisex')], max_length=50, null=True),
        ),
    ]
