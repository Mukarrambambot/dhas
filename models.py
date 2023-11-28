from database import db

class DiabeticUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(20), nullable=False)
    smoking = db.Column(db.Boolean, nullable=False)
    drinking = db.Column(db.Boolean, nullable=False)
    sugar_level = db.Column(db.Float)  
    hibic = db.Column(db.String(100))  
    chronic_disease = db.Column(db.String(100))  
    blood_sugar_level = db.Column(db.Float)
    insulin_level = db.Column(db.Integer)
    sleep_difficulties = db.Column(db.Boolean)
    sleep_hours = db.Column(db.Integer)
    diet_description = db.Column(db.Text)
    diet_goals = db.Column(db.Text)
    stress_management = db.Column(db.Text)
    stress_factors = db.Column(db.Text)

class NonDiabeticUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(20), nullable=False)
    smoking = db.Column(db.Boolean, nullable=False)
    drinking = db.Column(db.Boolean, nullable=False)

class OtherMedicalIssueUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(20), nullable=False)
    smoking = db.Column(db.Boolean, nullable=False)
    drinking = db.Column(db.Boolean, nullable=False)
    medical_issue_details = db.Column(db.Text)
