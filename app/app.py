from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'criador_driver')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)