from flask import Blueprint

helloWorld_bp = Blueprint('helloWorld', __name__)

@helloWorld_bp.route('/hello') 
def hello_world():     
    return 'hello world'