import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DATABASE_NAME = 'site.db'

def create_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Define your table schema here
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diabetic_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT,
        phone TEXT,
        gender TEXT,
        smoking INTEGER,
        drinking INTEGER,
        sugar_level REAL,  -- Add sugar_level column
        hibic TEXT,       -- Add hibic column
        chronic_disease TEXT,  -- Add chronic_disease column
        blood_sugar_level REAL,
        insulin_level INTEGER,
        sleep_difficulties INTEGER,
        sleep_hours INTEGER,
        diet_description TEXT,
        diet_goals TEXT,
        stress_management TEXT,
        stress_factors TEXT
    )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS non_diabetic_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            phone TEXT,
            gender TEXT,
            smoking INTEGER,
            drinking INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS other_medical_issue_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            phone TEXT,
            gender TEXT,
            smoking INTEGER,
            drinking INTEGER,
            medical_issue_details TEXT
        )
    ''')

    connection.commit()
    connection.close()

def init_db(app):
    if 'sqlalchemy' not in app.extensions:
        db.init_app(app)
        with app.app_context():
            db.create_all()

def create_connection():
    return db.create_engine(DATABASE_NAME)

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Define your table schema here
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diabetic_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT,
        phone TEXT,
        gender TEXT,
        smoking INTEGER,
        drinking INTEGER,
        sugar_level REAL,  -- Add sugar_level column
        hibic TEXT,       -- Add hibic column
        chronic_disease TEXT,  -- Add chronic_disease column
        blood_sugar_level REAL,
        insulin_level INTEGER,
        sleep_difficulties INTEGER,
        sleep_hours INTEGER,
        diet_description TEXT,
        diet_goals TEXT,
        stress_management TEXT,
        stress_factors TEXT
    )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS non_diabetic_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            phone TEXT,
            gender TEXT,
            smoking INTEGER,
            drinking INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS other_medical_issue_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            phone TEXT,
            gender TEXT,
            smoking INTEGER,
            drinking INTEGER,
            medical_issue_details TEXT
        )
    ''')
    # ... create tables for other user types ...

    connection.commit()
    connection.close()
