# Project Summary for CV

## Online Comic Reading Platform

**Stack:** Django 4.2.7, Python, HTML5, CSS3, JavaScript, Bootstrap 5, SQLite, Gunicorn, Pillow

**Description:** A full-stack comic reading web application featuring content management system, user interactions, and reading tracking. Built with Django framework to deliver seamless reading experience with organized content hierarchy and role-based access control.

**Key Modules:**

**Authentication & Authorization:** Implemented Django authentication system with role-based access control (Reader, Uploader, Admin), session management, and protected routes for content management

**Multi-level Content Management:** Designed hierarchical data structure (Series → Chapters → Pages) with Django ORM, enabling efficient content organization and navigation with ForeignKey and ManyToMany relationships

**Reading History & Favorites:** Built user engagement tracking system storing reading progress and favorite series using ManyToMany relationships, providing personalized user experience

**Image Upload & Storage:** Integrated Django FileField with media handling for multi-image uploads (cover images, background images, chapter pages), supporting efficient storage and retrieval of hundreds of images

**View Count Analytics:** Developed real-time statistics system calculating total views across chapters using Django property decorators and aggregation, providing insights for content creators

**Content Upload Interface:** Created intuitive admin interface for uploaders to manage series, add chapters, and upload page images with form validation and error handling

**Responsive Reader Interface:** Designed mobile-friendly reading interface with carousel navigation, optimized image loading, and smooth page transitions for enhanced user experience
