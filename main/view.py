from flask import Blueprint, render_template, request
from main.utils import search_in_post
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)

posts_blueprint = Blueprint('posts_blueprint', __name__, static_folder="static", template_folder="templates")

@posts_blueprint.route("/")
def profile_page():
    return render_template("index.html")


@posts_blueprint.route("/post_list/")
def search_post():

    s = request.args.get('s')
    logging.info(f"Слово для поиска: {s}")
    posts = search_in_post(s)
    return render_template("post_list.html", s=s, posts=posts)




