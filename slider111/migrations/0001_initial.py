# Generated by Django 2.1.2 on 2018-11-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('ma_slider', models.AutoField(primary_key=True, serialize=False)),
                ('ten_slider', models.CharField(max_length=100, unique=True, verbose_name='Tên slider')),
                ('tieu_de', models.CharField(max_length=100, unique=True, verbose_name='Tiêu đề')),
                ('hinh_slider', models.ImageField(upload_to='slider', verbose_name='Hình')),
                ('noi_dung', models.TextField(max_length=500, verbose_name='Tóm tắt')),
                ('url', models.CharField(max_length=200, unique=True)),
                ('trang_thai', models.BooleanField(default=True, verbose_name='Trạng thái')),
            ],
        ),
    ]
