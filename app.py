from flask import Flask
from main.view import posts_blueprint
from loader.view import load_blueprint


app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(load_blueprint)


app.run()

