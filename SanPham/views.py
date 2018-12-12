from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from SanPham.models import SanPham
from Slider.models import Slider
import re
from cart.forms import CartAddProductForm

# Create your views here.
def chi_tiet_san_pham(request, chuoi):
	arr = chuoi.split('-')
	key=arr[len(arr)-1]
	sanpham = SanPham.objects.get(ma_san_pham=key)
	lst_slider = Slider.objects.all()
	cart_product_form = CartAddProductForm()
	return render(request, 'SanPham/chi_tiet_san_pham.html', {'sanpham': sanpham,'lst_slider':lst_slider, 'cart_product_form': cart_product_form})

def san_pham_moi(request):
    sanpham_list = SanPham.objects.all()
    paginator = Paginator(sanpham_list, 12) # Show 12 SanPham per page

    page = request.GET.get('page')
    sanphams = paginator.get_page(page)
    lst_slider = Slider.objects.all()
    return render(request, 'SanPham/doc_ds_san_pham.html', {'sanphams_html': doc_dssp_to_htm(sanphams),'sanphams':sanphams,'lst_slider':lst_slider})

def san_pham_theo_loai(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def san_pham_phan_trang(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def doc_dssp_to_htm(DSSP):
    chuoiHTML=''
    for sp in DSSP:
        chuoiHTML+='<div class="col-lg-3">'
        chuoiHTML+='<div class="post_item post_v_med d-flex flex-column align-items-start justify-content-start">'
        chuoiHTML+='<div class="post_image"><img src="/media/'+str(sp.hinh_san_pham)+'" alt="https://unsplash.com/@oria_hector"></div>'
        chuoiHTML+='<div class="post_content">'
        chuoiHTML+='<div class="post_category cat_technology"><a href="/san-pham/'+bodau(sp.ten_san_pham)+'-'+str(sp.ma_san_pham)+'">'+ sp.ten_san_pham +'<br>'+ '{:,}'.format(sp.size_s) +'vnđ </a></a></div>'
        chuoiHTML+='<div class="post_text">'
        chuoiHTML+='<p>'+ sp.mo_ta_tom_tat +'</p>'
        chuoiHTML+='</div>'
        chuoiHTML+='</div>'
        chuoiHTML+='</div>'
        chuoiHTML+='</div>'
    return chuoiHTML

def bodau(str):
    str=str.lower()
    chuoi=re.sub(r' ','-',str)

    str_unicode = {'a':'á|à|ả|ã|ạ|ă|ắ|ặ|ằ|ẳ|ẵ|â|ấ|ầ|ẩ|ẫ|ậ','d':'đ','e':'é|è|ẻ|ẽ|ẹ|ê|ế|ề|ể|ễ|ệ',
    'i':'í|ì|ỉ|ĩ|ị','o':'ó|ò|ỏ|õ|ọ|ô|ố|ồ|ổ|ỗ|ộ|ơ|ớ|ờ|ở|ỡ|ợ','u':'ú|ù|ủ|ũ|ụ|ư|ứ|ừ|ử|ữ|ự',
    'y':'ý|ỳ|ỷ|ỹ|ỵ','A':'Á|À|Ả|Ã|Ạ|Ă|Ắ|Ặ|Ằ|Ẳ|Ẵ|Â|Ấ|Ầ|Ẩ|Ẫ|Ậ','D':'Đ','E':'É|È|Ẻ|Ẽ|Ẹ|Ê|Ế|Ề|Ể|Ễ|Ệ',
    'I':'Í|Ì|Ỉ|Ĩ|Ị','O':'Ó|Ò|Ỏ|Õ|Ọ|Ô|Ố|Ồ|Ổ|Ỗ|Ộ|Ơ|Ớ|Ờ|Ở|Ỡ|Ợ','U':'Ú|Ù|Ủ|Ũ|Ụ|Ư|Ứ|Ừ|Ử|Ữ|Ự',
    'Y':'Ý|Ỳ|Ỷ|Ỹ|Ỵ'}
    for item in str_unicode.items():
        chuoi=re.sub(item[1],item[0],chuoi)
    return chuoi