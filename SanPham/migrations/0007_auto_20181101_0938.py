# Generated by Django 2.1.2 on 2018-11-01 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SanPham', '0006_auto_20181101_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='loai_san_pham',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoaiSanPham.LoaiSanPham', verbose_name='Loại sản phẩm'),
        ),
    ]
