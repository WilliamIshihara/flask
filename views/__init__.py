#注册

from .views import blue
from .Two import Two

def regiest(app):
    app.register_blueprint(blue)
    app.register_blueprint(Two)
