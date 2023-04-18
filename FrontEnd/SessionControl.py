from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'my-secret-key'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}. <a href="/logout">Logout</a>'
    else:
        return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct (for example, by querying a database).
        # If they are correct, store the username in the session.
        if username == 'myusername' and password == 'mypassword':
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)