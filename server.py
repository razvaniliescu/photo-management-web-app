from flask import Flask, request, render_template, redirect, url_for, send_from_directory, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="public")
app.secret_key = "abcd"
app.config["extensions"] = {"png", "jpg", "jpeg", "webp"}
app.config["upload"] = "public/images"

admin_password = "abcd"

@app.route("/")
def index():
    categories = os.listdir(app.config["upload"])
    images = {category: os.listdir(os.path.join(app.config["upload"], category)) for category in categories}
    return render_template("index.html", images=images)

@app.route("/about")
def second():
    return render_template("aboutme.html", code=302)

@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = ""
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == admin_password:
            session["authenticated"] = True
            return redirect("/upload")
        error_msg = "Invalid Password!"
    return render_template("login.html", error_msg=error_msg)

@app.route("/logout")
def logout():
    session["authenticated"] = False
    return redirect("/")

@app.route("/about")
def about():
    return render_template("aboutme.html")

def allowed_image_extension(image_name):
    return "." in image_name and image_name.rsplit(".", 1)[1] in app.config["extensions"]

@app.route("/upload", methods=["GET", "POST"])
def upload():
    error_msg = ""
    if session["authenticated"] == False:
        return redirect("/login")
    if request.method == "POST":
        image = request.files["image"]
        new_name = request.form["image_name"]
        category = request.form["category"]
        if image and allowed_image_extension(image.filename):
            if new_name:
                image_name = new_name + "." + image.filename.rsplit('.', 1)[1]
            image_name = secure_filename(image.filename)
            category_path = os.path.join(app.config["upload"], category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            image.save(os.path.join(category_path, image_name))
            return redirect("/")
        else:
            error_msg = "Unsupported file type!"
    return render_template("upload.html", error_msg=error_msg)

@app.route("/delete/<category>/<image>")
def delete(category, image):
    image_path = os.path.join(app.config["upload"], category, image)
    os.remove(image_path)
    dir_path = os.path.join(app.config["upload"], category)
    dir = os.listdir(dir_path)
    if len(dir) == 0:
        os.rmdir(dir_path)
    return redirect("/")

@app.route("/display_image/<category>/<image>")
def display_image(category, image):
    return send_from_directory(os.path.join(app.config["upload"], category), image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

