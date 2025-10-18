# 💍 Mini Matrimonial Platform

This is a Django-based mini matrimonial platform that extracts and displays user profiles from sample HTML pages using **BeautifulSoup**.

The project demonstrates skills in:
- HTML parsing and data extraction
- Django ORM and model management
- REST API creation and frontend integration
- Clean, modular project structure

---

## 🚀 Features

- Parse HTML files containing profile data  
- Save extracted data to a Django database  
- Provide APIs for profile data  
- Display all profiles in a responsive web interface  
- Simple and reusable Django management command  

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django (Python) |
| Parsing | BeautifulSoup |
| Database | SQLite (default) |
| Frontend | HTML, Bootstrap |
| API | Django REST Framework (optional) |

---

## 🧩 Project Setup

### 1. Clone or extract the project
Unzip the assignment folder and open it in your code editor or terminal.

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (optional)
```bash
python manage.py createsuperuser
```

---

## 🗂️ Adding Sample Profiles

Place your sample HTML files inside the folder:
```
sample_profiles/
```

---

## 🧠 Running the Parser

To extract and save profile data to the database:
```bash
python manage.py parse_profiles --dir sample_profiles
```

Expected output:
```
✅ Saved: Aarti Patel (Ahmedabad)
✅ Saved: Rohit Sharma (Surat)
✅ Done. 2 profiles added.
```

---

## 🌐 Running the Application

Start the Django development server:
```bash
python manage.py runserver
```

Then open your browser and visit:
- **Frontend:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📦 Project Structure

```
matrimonial_project/
│
├── profiles/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── parse_profiles.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
│
├── sample_profiles/
│   ├── profile1.html
│   ├── profile2.html
│   └── ...
│
├── matrimonial/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

---

## 📄 Notes

- Works with structured HTML containing `class` attributes for each field.  
- Uses SQLite by default (no setup required).  
- Easily extendable for more attributes or APIs.  

---

## 🧑‍💻 Author

Developed by **Sadhu Kwinsi**  
For Django Practical Assessment — Mini Matrimonial Platform  
October 2025

---

## 📜 License

MIT License — Free for educational and personal use.
