from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('NEW.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Change 'email' to 'password'
        # Here you can perform any desired operations with the submitted data
        # For example, you can print it to the console
        print(f'Username: {username}, Password: {password}')  # Update print statement
        # Redirect to a success page or do any other necessary action
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
