from django.db import models
from LoaiSanPham.models import LoaiSanPham
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class SanPham(models.Model):
    ma_san_pham = models.AutoField(primary_key=True)
    ten_san_pham = models.CharField('Tên sản phẩm',max_length=100,  unique=True)
    loai_san_pham = models.ForeignKey(LoaiSanPham, on_delete=models.CASCADE, verbose_name = u'Loại sản phẩm')
    hinh_san_pham = models.ImageField("Hình",upload_to='hinh_san_pham', blank=True)
    size_s = models.FloatField()
    size_m = models.FloatField()
    giam_gia = models.FloatField("Giảm giá")
    mo_ta_tom_tat=models.CharField("Tóm tắt",max_length=200)
    mo_ta_chi_tiet=RichTextUploadingField("Chi tiết")
    trang_thai = models.BooleanField("Trạng thái",default=True)
    def __str__(self):
        return self.ten_san_pham