from flask import Flask

from views.__init__ import regiest

def init_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    regiest(app)
    return app


