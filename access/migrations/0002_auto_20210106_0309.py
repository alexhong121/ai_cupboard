# Generated by Django 3.1.1 on 2021-01-06 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ui_access',
            name='Features_id',
        ),
        migrations.AlterField(
            model_name='ui_access',
            name='Profiles_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profiles'),
        ),
    ]