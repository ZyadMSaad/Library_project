# 📖 Online Library Website

> **Cairo University — Faculty of Computers and Artificial Intelligence**
> Course: IS231 Web Technology | Project No. 2
> TA: Samaa Mohamed | **Group No. 1**

---

## 👥 Team Members

| Name | ID | Section | Responsible For |
|------|:--:|:-------:|----------------|
| 👑 **Haneen Ayman Mohammed** *(Leader)* | 20240174 | S12 | 🏠 Home Page & Navbar |
| 📂 **Doaa Hany Abd El Rahman** | 20240180 | S12 | 🗂️ Categories, Book Details & Admin: Manageable Categories |
| 📋 **Salma Mohsen Sayed** | 20240237 | S12 | ✅ Admin: List of Borrowed Books & List of Available Books |
| ✏️ **Sarah Mohamed Salah El-Din** | 20242150 | S12 | 🔍 Edit Form, Borrow Form & Search Bar |
| ⚙️ **Zyad Mohammed Saad** | 20242144 | S12 | ➕ Admin: Add & Delete Forms |
| 🔐 **Basel Mohammed Abd El Hakim** | 20240112 | S11 | 🔑 Sign Up & Login |

---

## 📌 Project Overview

A full-stack **Online Library Management System** built with **Django**. The system supports two roles:

- **User** — Browse books by category, view book details, search, and borrow books.
- **Admin** — Manage the full library: add, edit, delete books, manage categories, and track borrowed/available books.

---

## ✨ Features

### 👤 User Side
- **Home Page & Navbar** — Landing page with navigation links *(Haneen)*
- **Sign Up & Login** — User registration and authentication *(Basel)*
- **Book Categories** — Browse books by category *(Doaa)*
- **Book Details** — View detailed info for each book *(Doaa)*
- **Search Bar** — Search for books by title or author *(Sarah)*
- **Borrow Form** — Borrow an available book *(Sarah)*

### 🛠️ Admin Side
- **Manageable Categories** — Add and manage book categories *(Doaa)*
- **Add Book Form** — Add new books to the library *(Zyad)*
- **Delete Book Form** — Remove books from the library *(Zyad)*
- **Edit Book Form** — Update existing book details *(Sarah)*
- **Borrowed Books List** — View all currently borrowed books *(Salma)*
- **Available Books List** — View all available books in stock *(Salma)*

---

## 🗂️ Project Structure

```
library_project/
├── accounts/               # Sign Up & Login (Basel)
│   ├── models.py           # Profile model (extends Django User)
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── login.html
│       └── signup.html
│
├── home/                   # Home Page & Navbar (Haneen)
│   ├── views.py
│   ├── urls.py
│   └── templates/home/
│       ├── Home.html
│       └── parts/
│           ├── navbar.html
│           └── footer.html
│
├── products/               # Core Book & Borrow logic
│   ├── models.py           # Product & Borrow models
│   ├── views.py
│   ├── urls.py
│   └── templates/products/
│       ├── Books.html          # Category listing (Doaa)
│       ├── BookID.html         # Book details (Doaa)
│       ├── Search.html         # Search bar (Sarah)
│       ├── Borrow a Book.html  # Borrow form (Sarah)
│       ├── Edit books details.html  # Edit form (Sarah)
│       ├── add.html            # Add book (Zyad)
│       ├── delete.html         # Delete book (Zyad)
│       └── BorrowedBooks.html  # Borrowed/Available lists (Salma)
│
├── library/                # Project settings & main URLs
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

---

## 🗃️ Database Models

### `Product` (Book)
| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Book title |
| `book_id` | IntegerField | Unique book ID |
| `category` | CharField | Fantasy, Romance, Action, History, Religious, Science, Horror, Other |
| `author` | CharField | Author name |
| `language` | CharField | Book language (default: English) |
| `format` | CharField | E-book or Hardcopy |
| `description` | TextField | Book description |
| `image` | ImageField | Book cover image |
| `active` | BooleanField | Whether book is active |
| `borrowed` | BooleanField | Whether book is currently borrowed |

### `Borrow`
| Field | Type | Description |
|-------|------|-------------|
| `user_name` | CharField | Borrower's name |
| `user_id` | IntegerField | Borrower's ID |
| `book_id` | IntegerField | Borrowed book ID |
| `borrow_date` | DateField | Date borrowed (auto) |
| `return_date` | DateField | Expected return date |

### `Profile` (extends Django User)
| Field | Type | Description |
|-------|------|-------------|
| `user` | OneToOneField | Link to Django's built-in User |
| `is_admin` | BooleanField | Admin privileges flag |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd library_project

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install django pillow

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (admin)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open your browser at: **http://127.0.0.1:8000/**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python / Django |
| Frontend | HTML, CSS |
| Database | SQLite3 |
| Media | Pillow (image handling) |

---

## 📄 License

This project was developed for academic purposes at Cairo University — Faculty of Computers and Artificial Intelligence.
