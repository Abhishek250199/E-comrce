# Generated by Django 4.2.4 on 2023-09-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_gallary_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallary',
            name='Gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Unisex')], null=True),
        ),
    ]