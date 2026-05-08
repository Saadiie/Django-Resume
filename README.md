# Django Portfolio Website

A modern Django-based portfolio website with reusable templates, responsive pages, and a functional contact form integrated with Gmail SMTP email services.

---

# Features

- Django template inheritance
- Reusable base template
- Responsive navbar and footer
- Home, About, and Contact pages
- Contact form with validation
- Email sending functionality
- Gmail SMTP integration
- Clean Django project structure
- Beginner-friendly architecture

---

# Project Structure

```bash
Portfolio/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pages/
│   ├── migrations/
│   ├── templates/
│   │   └── pages/
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   │
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── base.html
│
├── manage.py
└── README.md



# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your_repository_url>
cd Portfolio
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

---

## 3. Activate Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

### Mac/Linux

```bash
source .venv/bin/activate
```

After activation you should see:

```bash
(.venv)
```

at the start of your terminal.

---

## 4. Install Dependencies

```bash
pip install django
```

---

## 5. Run Migrations

```bash
python manage.py migrate
```

---

# Configure Email Settings

Before running the contact form, you **MUST** update your Gmail credentials inside:

```bash
config/settings.py
```

Add the following configuration at the bottom of the file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_character_app_password'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = 'yourgmail@gmail.com'
```

---

# Important Note About Gmail Password

⚠️ **DO NOT** use your normal Gmail login password.

Google blocks direct SMTP login using normal passwords.

Instead, use a **Gmail App Password**.

---

# How to Generate Gmail App Password

## Step 1

Go to:

```text
https://myaccount.google.com/security
```

---

## Step 2

Enable:

- 2-Step Verification

---

## Step 3

Search for:

```text
App Passwords
```

---

## Step 4

Create a new app password for:

- App → Mail
- Device → Other

---

## Step 5

Google will generate a 16-character password like:

```text
abcd efgh ijkl mnop
```

Copy it and paste it **WITHOUT spaces**:

```python
EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'
```

---

# Run Development Server

```bash
python manage.py runserver
```

---

# Open Website

Visit:

```text
http://127.0.0.1:8000/
```

---

# Available Routes

| Page | URL |
|---|---|
| Home | `/` |
| About | `/about/` |
| Contact | `/contact/` |

---

# Contact Form Functionality

The contact page contains:

- Full Name
- Phone Number
- Email Address
- Message

When submitted:

- Django validates the form
- Email is sent to admin email
- Success message appears
- Form resets automatically

---

# Why We Used Django `send_mail` Instead of Python Built-in Email Module

This project uses:

```python
from django.core.mail import send_mail
```

instead of Python’s lower-level `smtplib` module.

---

## Reasons

### 1. Django Integration

Django mail system integrates directly with:

- `settings.py`
- environment configuration
- deployment setup
- Django apps

---

### 2. Cleaner Code

Using Django:

```python
send_mail(...)
```

is much shorter and cleaner than manually handling SMTP connections.

---

### 3. Easier Maintenance

Django automatically manages:

- SMTP connection
- TLS encryption
- authentication
- backend configuration

---

### 4. Better Scalability

Later this can easily be upgraded to:

- HTML emails
- asynchronous email sending
- password reset systems
- email verification
- bulk emails
- Celery integration

---

# Example of Python Built-in Email Module (Not Used)

Python built-in approach requires much more manual code:

```python
import smtplib
from email.mime.text import MIMEText
```

Django abstracts these lower-level details for cleaner development.

---

# Technologies Used

- Python
- Django
- HTML5
- CSS3
- SMTP Email Integration

---

# Development Notes

- Restart server after changing settings or templates
- Keep `.venv` activated while working
- Never upload real email passwords to GitHub
- Use environment variables in production

---

# Author

## SAAD MEHMOOD

Python Developer & AI Enthusiast