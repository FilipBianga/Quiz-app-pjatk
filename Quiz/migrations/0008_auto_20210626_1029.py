# Generated by Django 3.2.4 on 2021-06-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_alter_fizyka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='informatyka',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
