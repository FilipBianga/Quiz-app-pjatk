# Generated by Django 3.1.5 on 2021-05-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_quizmodel_totalques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matematyka',
            old_name='mat',
            new_name='mat',
        ),
        migrations.RenameField(
            model_name='fizyka',
            old_name='fiz',
            new_name='fiz',
        ),
        migrations.RenameField(
            model_name='historia',
            old_name='his',
            new_name='his',
        ),
        migrations.RenameField(
            model_name='informatyka',
            old_name='inf',
            new_name='inf',
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]
