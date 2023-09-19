from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    subprocess.call(f"adb -s emulator-5554 shell input tap 206 178", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=2020)