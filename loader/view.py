from flask import Flask, render_template, request, Blueprint, send_from_directory
from loader.utils import dump_content_in_json
from config import UPLOAD_FOLDER
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

load_blueprint = Blueprint("laod_blueprint", __name__, static_folder="static", template_folder="templates")


@load_blueprint.route("/post")
def load_post():
    return render_template("post_form.html")


@load_blueprint.route("/post_upload", methods=["POST", "GET"])
def upload_post():
    data = {}  # Словарь, куда будем записывать новые посты
    try:
        picture = request.files.get("picture")
        content = request.form.get("content")
        filename = picture.filename

        data["pic"] = UPLOAD_FOLDER + filename  #Записываем картинку в словарь в виде "/uploads/filename.jpg"
        data["content"] = content   #Записываем текст
        dump_content_in_json(data)   #Записываем словарь в JSON
        picture.save(f".{UPLOAD_FOLDER + filename}")
        if filename.split(".")[-1] not in ["jpg", "jpeg", "png"]:
            logging.info("Файл не изображение")

    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "<h1>Файл не найден</h1>"

    else:
        return render_template("post_uploaded.html", data=data)


@load_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


