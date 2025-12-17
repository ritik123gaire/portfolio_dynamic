# Dynamic Portfolio with Django

This is your portfolio website converted to a dynamic Django application. You can now manage all content through the Django admin panel!

## Features

- **Dynamic Content Management**: Edit everything through the admin panel
- **Profile Management**: Update your bio, tagline, and profile picture
- **Education & Experience**: Add/edit your education and work history
- **Skills**: Organize your skills by category
- **Services**: Showcase what you can do
- **Portfolio Projects**: Display your projects with images and categories
- **Blog Posts**: Share your thoughts and articles
- **Contact Form**: Receive messages from visitors
- **Statistics**: Display achievement numbers

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin username, email, and password.

### 4. Run the Development Server

```bash
python manage.py runserver
```

The site will be available at: http://127.0.0.1:8000/

### 5. Access Admin Panel

Go to: http://127.0.0.1:8000/admin/

Login with the superuser credentials you created.

## Adding Content

### Profile Information
1. Go to Admin Panel → Profile
2. Add/edit your profile information
3. Upload profile image
4. Add social media links

### Education
1. Go to Admin Panel → Education
2. Click "Add Education"
3. Fill in institution, degree, dates
4. Use "order" field to control display order

### Experience
1. Go to Admin Panel → Experience
2. Click "Add Experience"
3. Fill in company, position, dates
4. Check "current" if you're still working there

### Skills
1. Go to Admin Panel → Skills
2. Add skills and select category:
   - Programming Language
   - Database
   - Data Analysis Libraries
   - Web Frameworks
   - Other Tools

### Services
1. Go to Admin Panel → Services
2. Add the services you offer
3. Choose an icon class (e.g., 'icon-laptop', 'icon-layers')
4. Mark as active/inactive

### Projects
1. Go to Admin Panel → Projects
2. Click "Add Project"
3. Fill in title, description, category
4. Upload project image
5. Add project/GitHub URLs
6. Mark as "featured" for priority display

### Blog Posts
1. Go to Admin Panel → Blog Posts
2. Click "Add Blog Post"
3. Write your content and excerpt
4. Mark as "featured" for carousel display

### Statistics
1. Go to Admin Panel → Statistics
2. Add your achievement numbers
3. Choose icon classes (e.g., 'icon-trophy', 'icon-layers')

### Contact Messages
- View messages received through the contact form
- Mark as read/unread

## Project Structure

```
portfolio_project/          # Main Django project settings
├── settings.py            # Project configuration
└── urls.py               # Main URL routing

portfolio/                 # Portfolio app
├── models.py             # Database models
├── views.py              # View functions
├── admin.py              # Admin configuration
├── urls.py               # App URL routing
└── templates/            # HTML templates
    └── portfolio/
        └── index.html    # Main template

static/                    # Static files (CSS, JS, images)
├── css/
├── js/
├── img/
└── fonts/

media/                     # User uploaded files
├── profile/              # Profile images
└── projects/             # Project images
```

## Icon Classes Reference

Common icon classes you can use:
- `icon-laptop` - Web Development
- `icon-layers` - Projects/Layers
- `icon-pencil` - Design
- `icon-briefcase` - Business
- `icon-cloud` - Cloud
- `icon-clipboard` - Management
- `icon-trophy` - Awards
- `icon-tools` - Skills

## Deployment

For production deployment:

1. Update `settings.py`:
   - Set `DEBUG = False`
   - Add your domain to `ALLOWED_HOSTS`
   - Configure proper SECRET_KEY
   - Set up production database (PostgreSQL recommended)

2. Collect static files:
```bash
python manage.py collectstatic
```

3. Use a production server (Gunicorn, uWSGI)
4. Set up a reverse proxy (Nginx, Apache)

## Need Help?

- Django Documentation: https://docs.djangoproject.com/
- Admin Panel: Click on each section to add/edit content
- All changes are saved in the database and appear on your site immediately!

Enjoy your dynamic portfolio! 🚀
