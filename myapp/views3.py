from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Nguoidung
# Create your views here.

def index(request):
	return render(request, 'index.html')


def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Chuyển hướng về login sau khi đăng ký thành công
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            ten = form.cleaned_data.get('ten')
            
            # Lưu tên người dùng vào session để theo dõi trạng thái đăng nhập
            request.session['nguoidung'] = ten
            
            return redirect('home')  # Chuyển hướng về trang chủ sau khi đăng nhập thành công
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def dang_xuat(request):
    request.session.flush()  # Xóa tất cả session
    return redirect('home')
