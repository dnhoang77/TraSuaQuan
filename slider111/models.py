from django.db import models

# Create your models here.
class Slider(models.Model):
    ma_slider = models.AutoField(primary_key=True)
    ten_slider = models.CharField('Tên slider',max_length=100,unique=True)
    tieu_de = models.CharField('Tiêu đề',max_length=100,unique=True)
    hinh_slider = models.ImageField("Hình",upload_to='slider')
    noi_dung = models.TextField('Tóm tắt',max_length=500)
    url = models.CharField(max_length=200,unique=True)
    trang_thai = models.BooleanField("Trạng thái",default=True)
    def __str__(self):
        return self.ten_slider