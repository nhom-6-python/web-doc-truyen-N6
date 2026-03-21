# Web Đọc Truyện Tranh

Ứng dụng web đọc truyện tranh trực tuyến được xây dựng bằng Django Framework.

## Tính năng

- Đọc truyện tranh trực tuyến với giao diện thân thiện
- Quản lý truyện, chương và trang truyện
- Hệ thống người dùng với các vai trò khác nhau
- Theo dõi lịch sử đọc truyện
- Yêu thích truyện
- Thống kê lượt xem
- Upload và quản lý truyện (dành cho người đăng truyện)
- Hệ thống thông báo

## Công nghệ sử dụng

- **Backend**: Django 4.2.7
- **Database**: SQLite (có thể chuyển sang MySQL/PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Image Processing**: Pillow
- **Server**: Gunicorn (production)

## Cấu trúc dự án

```
.
├── myapp/              # Ứng dụng chính
│   ├── models.py       # Models: Truyen, Chap, Trang, Nguoidung, Thongbao
│   ├── views.py        # Views xử lý logic
│   ├── forms.py        # Forms cho các model
│   ├── templates/      # HTML templates
│   └── static/         # CSS, JS, images
├── myweb/              # Cấu hình Django project
│   ├── settings.py     # Cấu hình chính
│   └── urls.py         # URL routing
├── media/              # Thư mục lưu trữ ảnh upload
│   ├── anhbia/         # Ảnh bìa truyện
│   ├── anhnen/         # Ảnh nền truyện
│   └── anhchap/        # Ảnh các trang truyện
├── dev-fe/             # Frontend development files
├── db.sqlite3          # Database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Cài đặt

### Yêu cầu hệ thống

- Python 3.8+
- pip

### Các bước cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Tạo và kích hoạt môi trường ảo (khuyến nghị):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate  # Windows
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Chạy migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Tạo superuser (admin):
```bash
python manage.py createsuperuser
```

6. Chạy development server:
```bash
python manage.py runserver
```

7. Truy cập ứng dụng:
- Website: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Models

### Truyen (Truyện)
- Tên truyện, thể loại, mô tả, tác giả
- Ảnh bìa và ảnh nền
- Lượt thích, lượt xem (tính từ tổng lượt xem các chap)

### Chap (Chương)
- Số thứ tự, tên chương
- Lượt xem, thời gian đăng
- Liên kết với Truyen

### Trang
- Ảnh trang truyện
- Liên kết với Chap

### Nguoidung (Người dùng)
- Tên, mật khẩu, vai trò
- Danh sách yêu thích, lịch sử đọc
- Truyện đã đăng, thông báo

### Thongbao (Thông báo)
- Nội dung thông báo

## Sử dụng

### Đọc truyện
- Truy cập trang chủ để xem danh sách truyện
- Click vào truyện để xem chi tiết và danh sách chương
- Chọn chương để đọc

### Quản lý truyện (Admin/Uploader)
- Đăng nhập với tài khoản có quyền
- Upload truyện mới với ảnh bìa và ảnh nền
- Thêm chương và upload ảnh các trang

### Admin Panel
- Quản lý toàn bộ dữ liệu: truyện, chương, người dùng
- Xem thống kê lượt xem
- Quản lý thông báo

## Development

### Chạy tests
```bash
python manage.py test
```

### Tạo migrations mới
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect static files (production)
```bash
python manage.py collectstatic
```

## Production Deployment

Dự án đã được cấu hình với:
- Gunicorn cho WSGI server
- WhiteNoise cho static files
- Hỗ trợ MySQL/PostgreSQL

Cập nhật `settings.py` cho production:
- Đặt `DEBUG = False`
- Cấu hình `ALLOWED_HOSTS`
- Thay đổi `SECRET_KEY`
- Cấu hình database production

## Đóng góp

Mọi đóng góp đều được chào đón. Vui lòng tạo pull request hoặc báo cáo issues.

## License

[Thêm thông tin license của bạn]

## Liên hệ

[Thêm thông tin liên hệ của bạn]
