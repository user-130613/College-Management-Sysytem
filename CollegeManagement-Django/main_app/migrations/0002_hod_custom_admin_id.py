# Generated by Django 3.1.1 on 2024-06-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='custom_admin_id',
            field=models.IntegerField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
