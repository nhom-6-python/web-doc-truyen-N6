from django import forms
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung

class TruyenForm(forms.ModelForm):
	class Meta:
		model = Truyen
		fields = ["ten", "theloai", "mota", "tacgia", "anhbia", "anhnen"]

class ChapForm(forms.ModelForm):
	class Meta:
		model = Chap
		fields = ["stt", "ten", "truyen"]

class TrangForm(forms.ModelForm):
	class Meta:
		model = Trang
		fields = ["anh", "chap"]

class ThongbaoForm(forms.ModelForm):
	class Meta:
		model = Thongbao
		fields = ["noidung"]

class NguoidungForm(forms.ModelForm):
	class Meta:
		model = Nguoidung
		fields =  ["ten", "matkhau", "vaitro"]


class RegisterForm(forms.ModelForm):
    matkhau_xacnhan = forms.CharField(widget=forms.PasswordInput, label='Nhập lại mật khẩu')

    class Meta:
        model = Nguoidung
        fields = ['ten', 'matkhau', 'vaitro']
        widgets = {
            'matkhau': forms.PasswordInput(),
        }

    def clean_ten(self):
        ten = self.cleaned_data.get('ten')
        if Nguoidung.objects.filter(ten=ten).exists():
            raise forms.ValidationError("Tên đã tồn tại. Vui lòng chọn tên khác.")
        return ten

    def clean(self):
        cleaned_data = super().clean()
        matkhau = cleaned_data.get("matkhau")
        matkhau_xacnhan = cleaned_data.get("matkhau_xacnhan")

        if matkhau != matkhau_xacnhan:
            raise forms.ValidationError("Mật khẩu không khớp.")
        
        return cleaned_data


class LoginForm(forms.Form):
    ten = forms.CharField(max_length=255, label="Tên đăng nhập")
    matkhau = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")

    def clean(self):
        cleaned_data = super().clean()
        ten = cleaned_data.get("ten")
        matkhau = cleaned_data.get("matkhau")

        # Kiểm tra tên người dùng có tồn tại không
        try:
            user = Nguoidung.objects.get(ten=ten)
        except Nguoidung.DoesNotExist:
            raise forms.ValidationError("Tên đăng nhập không đúng.")

        # Kiểm tra mật khẩu có khớp không
        if user.matkhau != matkhau:
            raise forms.ValidationError("Mật khẩu không chính xác.")

        return cleaned_data
