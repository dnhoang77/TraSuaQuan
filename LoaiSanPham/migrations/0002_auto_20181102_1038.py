# Generated by Django 2.1.2 on 2018-11-02 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoaiSanPham', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaisanpham',
            name='trang_thai',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]