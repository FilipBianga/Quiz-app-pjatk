# Generated by Django 3.2.4 on 2021-06-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_matematyka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fizyka',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
