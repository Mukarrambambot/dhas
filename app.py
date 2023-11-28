from flask import Flask, render_template, request, redirect
from database import init_db, db
from models import DiabeticUser, NonDiabeticUser, OtherMedicalIssueUser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)

# Check if the email already exists in any of the tables
def check_email_exists(email):
    return (
        DiabeticUser.query.filter_by(email=email).first() or
        NonDiabeticUser.query.filter_by(email=email).first() or
        OtherMedicalIssueUser.query.filter_by(email=email).first()
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Extract user data from the form
        name = request.form.get('name')
        age = int(request.form.get('age'))
        email = request.form.get('email')

        # Check if the email already exists
        if check_email_exists(email):
            return 'Email address already exists'

        phone = request.form.get('phone')
        gender = request.form.get('gender')
        smoking = 'smoking' in request.form
        drinking = 'drinking' in request.form

        # Depending on the selected medical issue, capture the value for redirection
        medical_issue = request.form.get('medicalIssues')

        # Redirect to the corresponding page based on the medical issue
        if medical_issue == 'diabetic':
            return redirect('/diabetic')
        elif medical_issue == 'non-diabetic':
            return redirect('/non-diabetic')
        elif medical_issue == 'other-medical-issue':
            return redirect('/other-medical-issue')
        else:
            # Handle the case where the medical issue is not recognized
            return 'Invalid medical issue'

    except Exception as e:
        # Handle exceptions and log the error
        print(f'Error: {str(e)}')
        return 'An error occurred'

@app.route('/diabetic', methods=['GET', 'POST'])
def diabetic():
    try:
        if request.method == 'POST':
            # Handle any specific form submission logic for the diabetic page here
            # For example, process form data related to diabetic-specific questions
            return render_template('Diabetic.html')  # Render the Diabetic.html template after processing the form

        return render_template('Diabetic.html')

    except Exception as e:
        # Handle exceptions and log the error
        print(f'Error: {str(e)}')
        return 'An error occurred'

@app.route('/non-diabetic', methods=['GET', 'POST'])
def non_diabetic():
    try:
        # Redirect to the thank-you page for both GET and POST requests
        return redirect('/thank-you')

    except Exception as e:
        # Handle exceptions and log the error
        print(f'Error: {str(e)}')
        return 'An error occurred'

@app.route('/other-medical-issue', methods=['GET', 'POST'])
def other_medical_issue():
    try:
        # Redirect to the thank-you page for both GET and POST requests
        return redirect('/thank-you')

    except Exception as e:
        # Handle exceptions and log the error
        print(f'Error: {str(e)}')
        return 'An error occurred'


@app.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    try:
        if request.method == 'POST':
            additional_comments = request.form.get('additionalComments')
            # Process additional comments if needed

            # For simplicity, let's just redirect to the main page
            return redirect('/')

        return render_template('thank_you.html')

    except Exception as e:
        # Handle exceptions and log the error
        print(f'Error: {str(e)}')
        return 'An error occurred'

if __name__ == '__main__':
    app.run(debug=True)
