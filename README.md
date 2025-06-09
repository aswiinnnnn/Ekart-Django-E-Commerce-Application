# 🛒 Ekart: A Basic E-commerce Web Application

## 📌 Overview

Ekart is a foundational e-commerce web application built using Django. It provides essential features like product browsing, shopping cart, user login, and a basic checkout system. This is ideal for learning how to build dynamic web apps with Django.

---

## 🚀 Features

### 👤 User Authentication
- User registration, login, and logout  
- Customer profiles linked to users

### 🛍️ Product Catalog
- Product listings with image, title, and price  
- Individual product detail pages

### 🛒 Shopping Cart
- Add/remove items  
- Update item quantity  
- Auto calculation of subtotal, tax, and total  
- Displays empty cart message

### 📦 Order Processing
- Simple checkout system  
- Order summary with ID, total, delivery, and address

### 📱 Responsive Navigation
- Hamburger menu for mobile  
- Dynamic links: Home, Products, Login/Logout, Cart

---

## 🧰 Technologies Used

### Backend
- Python 3.9+
- Django 4.2.x
- SQLite (can be replaced with PostgreSQL)

### Frontend
- HTML5, CSS3 (responsive)
- JavaScript (basic interactivity)
- Font Awesome (icons)

### Others
- `pip` (dependencies)
- `python-dotenv` (for `.env` config)

---

## 🛠️ Getting Started

### 📋 Prerequisites
- Python 3.9+  
- `pip` installed  

---

### 🔄 1. Clone the Repository

```bash
git clone https://github.com/aswiinnnnn/Ekart-Django-E-Commerce-Application
cd ekart

### 🧪 2. Create Virtual Environment

```bash
python -m venv venv

# For Windows:
.\venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, you can create it with:
```bash
pip freeze > requirements.txt
```

---

### 🔐 4. Configure Environment Variables

1. Create a `.env` file in the root directory (where `manage.py` is)
2. Move your secret key from `settings.py` into `.env`:
   ```env
   SECRET_KEY='your-secret-key-here'
   ```
3. Make sure `.env` is included in `.gitignore`

---

### 🧱 5. Apply Database Migrations

```bash
python manage.py makemigrations orders
python manage.py migrate
```

---

### 👨‍💼 6. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

---

### ▶️ 7. Start Development Server

```bash
python manage.py runserver
```

Visit your site at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 🔑 8. Access Django Admin

Login at:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Use the superuser credentials you created.

