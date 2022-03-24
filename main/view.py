from flask import Blueprint, render_template, request
from functions import read_from_json, search_in_post

posts_blueprint = Blueprint('posts_blueprint', __name__)

@posts_blueprint.route("/")
def profile_page():
    return render_template("index.html")


@posts_blueprint.route("/post_list/")
def search_post():

    s = request.args.get('s')
    data = search_in_post(s)
    return render_template("post_list.html", s=s, data=data)

