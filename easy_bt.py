from flask import Flask, render_template, request,json
from bt2magnet import bt2magnet
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files['file']
        dir = app.config["UP_DIR"]+f.filename
        if not os.path.exists(app.config["UP_DIR"]):
            os.makedirs(app.config["UP_DIR"])
            os.chmod(app.config["UP_DIR"], 777)
        f.save(dir)
        magnet = bt2magnet(dir)
        return magnet
    return "err"


if __name__ == '__main__':
    app.run()
