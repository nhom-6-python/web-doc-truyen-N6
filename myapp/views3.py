from django.shortcuts import render, redirect
from .forms import NguoidungForm
from .models import Nguoidung
# Create your views here.

def index(request):
	return render(request, 'index.html')


def registerPage(request):
    if request.method == 'POST':
        form = NguoidungForm(request.POST)
        ten = request.POST['ten']
        mk = request.POST['matkhau']
        nhaplaimk = request.POST['nhaplaimk']
        nguoiDungList = Nguoidung.objects.values_list('ten', flat = True)
        
        if form.is_valid() and mk == nhaplaimk and ten not in nguoiDungList:
            form.save()
            return redirect('login')  # Chuyển hướng về login sau khi đăng ký thành công

    else:
        form = NguoidungForm()
    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = NguoidungForm(request.POST)
            # Lấy dữ liệu từ form
        ten = request.POST['ten']
        matkhau = request.POST['matkhau']
        nguoiDungList = Nguoidung.objects.values_list('ten', 'matkhau')
        # Lưu tên người dùng vào session để theo dõi trạng thái đăng nhập
        if (ten, matkhau) in nguoiDungList:
            request.session['nguoidung'] = ten
            
            return redirect('home')  # Chuyển hướng về trang chủ sau khi đăng nhập thành công
    else:
        form = NguoidungForm()

    return render(request, 'login.html', {'form': form})

def dang_xuat(request):
    request.session.flush()  # Xóa tất cả session
    return redirect('home')
