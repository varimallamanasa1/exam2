from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return redirect(url_for('greet', username=name))
@app.route('/greet/<username>')     
def greet(username):
    return f'Hello, {username}!'        
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')