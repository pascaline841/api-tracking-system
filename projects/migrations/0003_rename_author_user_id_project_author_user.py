# Generated by Django 3.2.4 on 2021-06-22 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='author_user_id',
            new_name='author_user',
        ),
    ]