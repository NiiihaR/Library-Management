Library Management System (Flask + SQLAlchemy)

Welcome to my Library Management System project! This is a simple web application built using Flask, SQLAlchemy, HTML, and CSS. It allows you to add, view, edit, and delete books from a small library database.

------------------------------------------------------------
Features
------------------------------------------------------------
- Add new books with title, author, year, and ISBN
- View all books in a clean table layout
- Edit any existing book
- Delete books safely
- SQLite database (created automatically)
- Simple, beginner-friendly structure

------------------------------------------------------------
Tech Stack
------------------------------------------------------------
- Python 3
- Flask
- Flask-SQLAlchemy
- HTML / CSS
- SQLite
- VS Code

------------------------------------------------------------
Project Structure
------------------------------------------------------------
library-management/
│── app.py
│── models.py
│── static/
│   └── style.css
│── templates/
│   ├── base.html
│   ├── book_list.html
│   ├── add_book.html
│   └── edit_book.html
│── requirements.txt
│── README.md
│── venv/

------------------------------------------------------------
How to Run the Project
------------------------------------------------------------

1. Clone or download the project.

2. Create a virtual environment  
   Windows:
   python -m venv venv  
   macOS/Linux:
   python3 -m venv venv  

3. Activate the environment  
   Windows:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  
   venv\Scripts\activate  
   macOS/Linux:
   source venv/bin/activate  

4. Install packages  
   pip install -r requirements.txt  

5. Run the app  
   python app.py  

6. Open in browser  
   http://127.0.0.1:5000

