# SWAMI KARUPPASWAMI THUNNAI

import socket
from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("file")
    for file in files:
        file.save(file.filename)
    return redirect("/")


@app.route("/download")
def download():
    return send_file("download.mp4")


if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), debug=True)
