import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
