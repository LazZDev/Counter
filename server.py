# Import necessary modules from the Flask library
from flask import Flask, render_template, request, redirect, session

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for the Flask app to securely handle sessions
app.secret_key = 'super_secret_key'

# Define the root route ("/") and its corresponding function


@app.route('/')
def index():
    # Check if 'visits' key is not in the session dictionary
    if 'visits' not in session:
        # Initialize the 'visits' key in the session dictionary with a value of 0
        session['visits'] = 0
    # Increment the 'visits' value by 1
    session['visits'] += 1
    # Render the 'index.html' template and pass the 'visits' value to it
    return render_template('index.html', visits=session['visits'])

# Define the "/destroy_session" route and its corresponding function


@app.route('/destroy_session')
def destroy_session():
    # Clear the session data
    session.clear()
    # Redirect the user to the root route ("/")
    return redirect('/')

# Define the "/add" route with the POST method and its corresponding function


@app.route('/add', methods=['POST'])
def add():
    # Get the 'increment' value from the submitted form and convert it to an integer
    increment = int(request.form['increment'])
    # Increment the 'visits' value by the specified increment value minus 1
    session['visits'] += increment - 1
    # Redirect the user to the root route ("/")
    return redirect('/')


# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Run the Flask app with debug mode enabled
    app.run(debug=True)
