# Generated by Django 5.1 on 2025-04-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_message_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='<NAME>', max_length=800),
        ),
    ]
