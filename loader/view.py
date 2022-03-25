from flask import Flask, render_template, request, Blueprint, send_from_directory
from functions import dump_content_in_json
load_blueprint = Blueprint("laod_blueprint", __name__)


@load_blueprint.route("/post")
def load_post():
    return render_template("post_form.html")


@load_blueprint.route("/post_upload", methods=["POST", "GET"])
def upload_post():
    if request.method == "POST":
        data = {} #Словарь, куда будем записывать новые посты
        picture = request.files.get("picture")
        content = request.form.get("content")
        filename = picture.filename
        picture.save(f"./uploads/{filename}")


        data["pic"] = "/" + filename  #Записываем картинку в словарь в виде "/uploads/filename.jpg"
        data["content"] = content   #Записываем текст
        dump_content_in_json(data)   #Записываем словарь в JSON

        return render_template("post_uploaded.html", data=data)
    else:
        return "Ошибка загрузки"


@load_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
