# Generated by Django 4.0.5 on 2023-03-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='averageRating',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='pageCount',
            field=models.CharField(max_length=100),
        ),
    ]