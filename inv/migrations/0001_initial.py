# Generated by Django 3.1.1 on 2020-12-30 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locker', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unit', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('written_date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(default='', upload_to='images/inv/')),
                ('name', models.CharField(default=None, max_length=50)),
                ('code', models.CharField(default=None, max_length=20, null=True)),
                ('form', models.CharField(default=None, max_length=100, null=True)),
                ('attribute', models.CharField(default=None, max_length=50, null=True)),
                ('remark', models.CharField(default=None, max_length=200, null=True)),
                ('Lockers_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locker.lockers')),
                ('Product_cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.product_category')),
                ('create_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_product_create_uid', to=settings.AUTH_USER_MODEL)),
                ('write_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_product_write_uid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('written_date', models.DateTimeField(auto_now=True, null=True)),
                ('initial_value', models.IntegerField(default=0)),
                ('out_value', models.IntegerField(default=0)),
                ('in_value', models.IntegerField(default=0)),
                ('remark', models.CharField(default=None, max_length=200, null=True)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.product')),
                ('create_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_stock_create_uid', to=settings.AUTH_USER_MODEL)),
                ('write_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_stock_write_uid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
