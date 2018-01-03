from flask import Flask

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='10.8.54.139', port=88)