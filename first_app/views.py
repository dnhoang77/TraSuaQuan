from django.shortcuts import render
from django.http import HttpResponse
from Slider.models import Slider
from SanPham.models import SanPham
# Create your views here.
def index(request):
    lst_slider = Slider.objects.all()
    lst_tra_sua = SanPham.objects.filter(loai_san_pham_id=1).all()
    lst_tra_sua_2=[]
    for item in lst_tra_sua:
        lst_tra_sua_2.append(item.__dict__)
    lst_topping = SanPham.objects.filter(loai_san_pham_id=8).all()[:3]

    lst_nuoc_ep_trai_cay = SanPham.objects.filter(loai_san_pham_id=6).all()
    lst_ca_phe = SanPham.objects.filter(loai_san_pham_id=7).all()
    context = {'lst_slider': lst_slider,'lst_tra_sua': lst_tra_sua_2,'lst_nuoc_ep_trai_cay':lst_nuoc_ep_trai_cay,'lst_ca_phe':lst_ca_phe,'lst_topping':lst_topping} 
    return render(request,"first_app/homepages.html", context)    
