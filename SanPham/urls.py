from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.san_pham_moi, name='index'),
    # ex: /polls/5/
    path('<slug:chuoi>/', views.chi_tiet_san_pham, name='chi tiết'),
    # ex: /polls/5/results/
    path('<int:question_id>/page/', views.san_pham_phan_trang, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/loai-san-pham/', views.san_pham_theo_loai, name='vote'),
]