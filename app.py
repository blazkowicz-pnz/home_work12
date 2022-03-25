from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.view import posts_blueprint
from loader.view import load_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(load_blueprint)
# @app.route("/")
# def page_index():
#     return render_template("index.html")
#
#
# @app.route("/list")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
#
#
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)

if __name__ =='__main__':
    app.run()

