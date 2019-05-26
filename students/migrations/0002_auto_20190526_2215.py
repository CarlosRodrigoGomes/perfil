# Generated by Django 2.2.1 on 2019-05-26 22:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
