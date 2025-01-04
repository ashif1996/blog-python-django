# 📰 TechCorner - A Dynamic Blog Platform  

TechCorner is a simple and dynamic blog platform built with **Python** and **Django**. It allows users to create, read, update, and delete blog posts, manage categories, and engage with content through comments. 

## 🚀 Features  
- **User Authentication**:  
  - Register, log in, and manage user profiles.  
- **Blog Management**:  
  - Create, update, delete, and view blog posts.  
- **Category Management**:  
  - Add and view categories for blog organization.  
- **Comment System**:  
  - Add comments to posts for community engagement.  

## 🛠️ Tech Stack  
- **Backend**: Python (Django Framework)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite  

## 📂 Project Structure  

```plaintext
blog-python-django/
├── .idea/                     # IDE configuration files
├── TechCorner/                # Django project configuration
│   ├── __pycache__/           # Compiled Python files
│   ├── __init__.py            # Initialization file
│   ├── asgi.py                # ASGI application
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL routing for the project
│   ├── wsgi.py                # WSGI application
├── static/tech/               # Static files for the project
│   ├── css/                   # CSS files
│   │   └── style.css          # General styles
│   ├── images/                # Image assets
├── tech/                      # Main blog application
│   ├── __pycache__/           # Compiled Python files
│   ├── migrations/            # Database migrations
│   ├── templates/             # Tech-specific templates
│   │   ├── add_category.html  # Add category page
│   │   ├── add_comment.html   # Add comment page
│   │   ├── add_post.html      # Add blog post page
│   │   ├── article_details.html # Blog post details page
│   │   ├── base.html          # Base template layout
│   │   ├── categories.html    # List of categories page
│   │   ├── delete_post.html   # Delete blog post page
│   │   ├── index.html         # Home page
│   │   └── update_post.html   # Update blog post page
│   ├── __init__.py            # Initialization file
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py                # App configuration
│   ├── forms.py               # Forms for the tech app
│   ├── models.py              # Models for the tech app
│   ├── tests.py               # Unit tests for the tech app
│   ├── urls.py                # URL routing for the tech app
│   └── views.py               # Views for the tech app
├── users/                     # User management application
│   ├── __pycache__/           # Compiled Python files
│   ├── migrations/            # Database migrations
│   ├── templates/registration/ # User-specific templates
│   │   ├── change-password.html  # Password change page
│   │   ├── create_user_profile.html # Create profile page
│   │   ├── edit_profile.html   # Edit profile form
│   │   ├── edit_profile_page.html # Edit profile page
│   │   ├── login.html          # Login page
│   │   ├── password_success.html # Password success page
│   │   ├── register.html       # Registration page
│   │   └── user_profile.html   # User profile page
│   ├── __init__.py             # Initialization file
│   ├── admin.py                # Admin panel configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Forms for user management
│   ├── models.py               # Models for user management
│   ├── tests.py                # Unit tests for user management
│   ├── urls.py                 # URL routing for user management
│   └── views.py                # Views for user management
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django's management script
```

## 🔧 Setup and Installation  

### Prerequisites  
- Python 3.8+  
- Django 4.0+  
- pip (Python package manager)  

### Steps  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/blog-python-django.git
   cd blog-python-django
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the server**:  
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/` to view the app.

## 📜 Usage  

- **Home Page**: Explore recent blog posts.  
- **Categories**: Browse posts by categories.  
- **Blog Post Management**:  
  - Create, edit, and delete blog posts.  
- **User Profiles**:  
  - View and edit user profiles.  

## 🌱 Learning Outcomes  

- Understanding Django's core features and MVC architecture.  
- Implementing authentication and user profile management.  
- Handling forms and file uploads.  
- Structuring a multi-app Django project.  

## 📜 License  

This project is licensed under the **MIT License**.

## 🌟 Acknowledgements  

- Thanks to the Django community for their extensive documentation and support.    

Happy Blogging! 😊  