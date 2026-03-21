# Online Comic Reading Platform

A web application for reading comics online built with Django Framework.

## Features

- Read comics online with user-friendly interface
- Manage series, chapters, and pages
- User system with role-based access control
- Reading history tracking
- Favorite series management
- View count statistics
- Upload and manage comics (for content uploaders)
- Notification system

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (MySQL/PostgreSQL support)
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Image Processing**: Pillow
- **Server**: Gunicorn (production)

## Project Structure

```
.
├── myapp/              # Main application
│   ├── models.py       # Models: Truyen, Chap, Trang, Nguoidung, Thongbao
│   ├── views.py        # Views handling logic
│   ├── forms.py        # Forms for models
│   ├── templates/      # HTML templates
│   └── static/         # CSS, JS, images
├── myweb/              # Django project configuration
│   ├── settings.py     # Main settings
│   └── urls.py         # URL routing
├── media/              # Uploaded images storage
│   ├── anhbia/         # Comic cover images
│   ├── anhnen/         # Background images
│   └── anhchap/        # Chapter page images
├── dev-fe/             # Frontend development files
├── db.sqlite3          # Database
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Installation

### System Requirements

- Python 3.8+
- pip

### Setup Steps

1. Clone repository:
```bash
git clone <repository-url>
cd <project-folder>
```

2. Create and activate virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access the application:
- Website: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Database Models

### Truyen (Series)
- Series name, genre, description, author
- Cover image and background image
- Like count, view count (calculated from total chapter views)

### Chap (Chapter)
- Chapter number, chapter name
- View count, publish date
- Foreign key to Truyen

### Trang (Page)
- Page image
- Foreign key to Chap

### Nguoidung (User)
- Username, password, role
- Favorites list, reading history
- Uploaded series, notifications

### Thongbao (Notification)
- Notification content

## Usage

### Reading Comics
- Access homepage to browse comic series
- Click on a series to view details and chapter list
- Select a chapter to start reading

### Managing Content (Admin/Uploader)
- Login with authorized account
- Upload new series with cover and background images
- Add chapters and upload page images

### Admin Panel
- Manage all data: series, chapters, users
- View statistics and analytics
- Manage notifications

## Development

### Run tests
```bash
python manage.py test
```

### Create new migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect static files (production)
```bash
python manage.py collectstatic
```

## Production Deployment

The project is configured with:
- Gunicorn for WSGI server
- WhiteNoise for static files
- MySQL/PostgreSQL support

Update `settings.py` for production:
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Change `SECRET_KEY`
- Configure production database

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or report issues.

## License

[Add your license information]

## Contact

[Add your contact information]
