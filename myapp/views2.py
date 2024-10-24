from django.shortcuts import render, redirect

# phuc
from django.shortcuts import render, redirect
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung
from .forms import TruyenForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.utils import timezone
from django.db.models import Sum,Q, Value
from django.db.models.functions import Coalesce

def list_thong_bao(request):
    ten_nguoi_dung=request.session.get('nguoidung',None)
    nguoidung=Nguoidung()
    nguoi_dungs= Nguoidung.objects.all()
    for x in nguoi_dungs:
        if x.ten==ten_nguoi_dung:
            nguoidung=x
    print(nguoidung)
    return nguoidung.thongbao.all()

def home(request): # view trang home
	top3 = top3_by_like()
	list_new_update = new_update()
	list_top_view = list()
	list_top_nhomdich = list()
	list_top_view_tuan = top_view('tuan')
	list_top_view_thang = top_view('thang')
	list_top_view_moiluc = top_view('moiluc')
	list_top_nhomdich_tuan = top_nhomdich('tuan')
	list_top_nhomdich_thang = top_nhomdich('thang')
	list_top_nhomdich_moiluc = top_nhomdich('moiluc')
	list_thong_baos = list_thong_bao(request)
	context = {
		'top3' : top3,
		'list_new_update': list_new_update,
		'list_top_view': list_top_view,
		'list_top_nhomdich': list_top_nhomdich,
		'list_top_view_tuan' : list_top_view_tuan,
		'list_top_view_thang' : list_top_view_thang,
		'list_top_view_moiluc' : list_top_view_moiluc,
		'list_top_nhomdich_tuan' : list_top_nhomdich_tuan,
		'list_top_nhomdich_thang' : list_top_nhomdich_thang,
		'list_top_nhomdich_moiluc' : list_top_nhomdich_moiluc,
		'list_thong_baos' : list_thong_baos,
	}
	
	return render(request, 'home.html', context)