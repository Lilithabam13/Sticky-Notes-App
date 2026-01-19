# 📝 Django Sticky Notes App

A beginner-friendly Django web application that allows users to create, view, update, complete, pin, and delete sticky notes.

This project demonstrates core Django concepts such as **models**, **views**, **forms**, **URL routing**, **templates**, **static files**, and **automated tests**. It is suitable for learning purposes and a small portfolio project.
---

## 🚀 Features

* Create new sticky notes
* View a list of all sticky notes
* View details of a single sticky note
* Update existing sticky notes
* Delete sticky notes
* Mark sticky notes as completed
* Pin important sticky notes (pinned notes appear first)
* Automated unit tests for views

---

## 🛠️ Technologies Used

* **Python 3**
* **Django**
* **SQLite** (default development database)
* **HTML & CSS** (Django templates & static files)

---

## 📂 Project Structure

```
Sticky_Notes_App_1/
|-- manage.py
|-- posts/
|   |-- migrations/
|   |-- static/posts/
|   |-- templates/posts/
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- static/
|-- sticky_notes_app_1/
|  |-- settings.py
|  |-- urls.py
|  |-- asgi.py
|  |-- wsgi.py
|-- .gitignore
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Lilithabam13/Sticky-Notes-App.git
cd Sticky-Notes-App
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / WSL / macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

Visit the app in your browser at:

👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Running Tests

This project includes automated tests for key views.

Run all tests with:

```bash
python manage.py test
```

---

## 📌 Notes on Version Control

* The **SQLite database (`db.sqlite3`)** is excluded from version control
* **Virtual environments** are excluded via `.gitignore`
* Django-generated admin static files are not tracked

To keep the repository clean and production-ready.

---

## 📖 Learning Outcomes

Through this project, the following Django concepts are demonstrated:

* MVC (Model–View–Template) architecture
* Django ORM and models
* Function-based views
* ModelForms
* URL routing and reverse lookups
* Static files and templates
* Writing and running Django tests
* Git & GitHub best practices

---

## 👩‍💻 Author

**Lilitha Bam**

---

## 📄 License

This project is intended for educational purposes.
