# Generated by Django 4.2 on 2023-04-18 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fitnes", "0005_remove_session_direction_catsession_direction"),
    ]

    operations = [
        migrations.RenameField(
            model_name="session", old_name="name", new_name="session",
        ),
    ]
