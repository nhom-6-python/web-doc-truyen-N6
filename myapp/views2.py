#Phuc
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
    return nguoidung.thongbao.all()
