# Generated by Django 3.2.4 on 2021-06-22 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_rename_author_user_id_issue_author_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='project_id',
            new_name='project',
        ),
    ]