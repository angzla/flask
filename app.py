# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'YAYYYY flask container'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='1024')
