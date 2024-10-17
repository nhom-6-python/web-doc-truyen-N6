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




