# Generated by Django 4.2.4 on 2023-09-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_gallary_category_alter_gallary_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.EmailField(max_length=50)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
