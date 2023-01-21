# Easy Share
*A Simple file sharing solution for quicky sharing files from your iPhone / Android / Other PC to your computer*

![](https://i.imgur.com/x1s97oT.png)

I Recently purchased an iPhone for my personal use. When I tried to transfer my pictures to my computer I came to realize that I need to be having an iTunes account or I need to be using some 3rd party software (which I am very skeptical) and the official solutions will be using internet to transfer files from my iphone to my computer which takes some time and it has its own limitations. Other tools like Whatsapp will compress my images and it is very messy.

I wanted to have a very simple solution to transfer files as fast as possible and it should be as simple as possible. My idea is to create a simple web application for uploading files in python which will be running our local network (e.g using Wifi) in 5000 port and connecting my iPhone to the same Wifi to access the web application to upload the files I want to share it to my computer 

Below is the Python script using Flask framwork for uploading the files

```python
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

if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), debug=True)
```

You will be needing to execute the easy_share.py script in your computer which needs to be receiving the files. Your computer needs to be having Python 3.x installed with Flask framework. You can use

```
pip install Flask
```

to install Flask on your machine. One other condition is **both the devices needs to be in the same network (e.g connected to same Wifi)**
Once the easy_share.py script is executed, You can access the web application in your iPhone using the URL displayed in your console. For example in my case:
![](https://i.imgur.com/OECX9C5.png)
The URL is: http://192.168.0.2:5000/

And from there you can simply browse the files you need to share and upload directly your computer. The files will be present in same place where the Python script (easy_share.py) is present

![](https://i.imgur.com/uuKjABO.png)
