# Generated by Django 5.1.6 on 2025-03-28 15:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleraccount',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
