# main.py
from flask import Flask
from Core_Modules.user_interface import ui_blueprint
import logging

app = Flask(__name__)
app.register_blueprint(ui_blueprint)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
