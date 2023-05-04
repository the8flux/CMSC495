from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Replace with your own secret key

@app.route('/logout')
def logout():
    # Remove the 'username' key from the session instance
    session.pop('username', None)
    # Redirect the user to the login page
    return redirect(url_for('login'))