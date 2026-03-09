import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Folder jisko host karna hai
BASE_DIR = os.path.join(os.path.dirname(__file__), "shared")

if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

@app.route("/")
def index():
    files = os.listdir(BASE_DIR)
    file_data = []

    for file in files:
        path = os.path.join(BASE_DIR, file)
        file_data.append({
            "name": file,
            "is_dir": os.path.isdir(path),
            "size": os.path.getsize(path) if os.path.isfile(path) else "-"
        })

    return render_template("index.html", files=file_data)

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(BASE_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)