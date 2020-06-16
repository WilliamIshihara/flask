from flask import Blueprint
from flask import render_template


Two = Blueprint('Two', __name__)

@Two.route('/<int:name1>/<method>/<int:name2>')
def say_Hi(method,name1,name2):
    if method =='+':
        return str(name1+name2)
    if method =='-' :
        return str(name1-name2)
    if method =='*':
        return str(name1*name2)
    if method =='%':
        return str(name1/name2)



