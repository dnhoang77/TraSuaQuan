from django.db import models

# Create your models here.
class LoaiSanPham(models.Model):
    id_loai_san_pham = models.AutoField(primary_key=True)
    ten_loai_san_pham = models.CharField(max_length=100,  unique=True)
    hinh_loai_san_pham=models.FileField(upload_to='hinh_loai_san_pham', blank=True)
    ghi_chu = models.CharField(max_length=500, blank=True)
    trang_thai = models.BooleanField(blank=True, default=True)
    def __str__(self):
        return self.ten_loai_san_pham