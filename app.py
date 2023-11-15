from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
correct_email = "christianealtayar@gmail.com"
correct_password = "soen357"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == correct_email and password == correct_password:
        # Successful login, redirect to a welcome page or home page
        return redirect(url_for('welcome'))
    else:
        # Failed login, show an error message
        error_message = "Invalid credentials. Please try again."
        return render_template('index.html', error_message=error_message)

@app.route('/welcome')
def welcome():
    return "Welcome to the website!"

if __name__ == '__main__':
    app.run(debug=True)
