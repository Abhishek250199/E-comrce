# Generated by Django 4.2.4 on 2023-09-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('ColorName', models.CharField(max_length=50)),
                ('Image', models.ImageField(max_length=50, upload_to='')),
            ],
        ),
    ]