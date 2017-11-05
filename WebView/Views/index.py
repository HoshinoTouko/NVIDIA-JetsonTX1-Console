from Modules.CarController import CarController
from flask import Blueprint, session, request, render_template, redirect, url_for

INDEX = Blueprint('index', __name__)

@INDEX.route('/')
def index():
    return render_template('index/index.html')

@INDEX.route('/setTime', methods=["GET", "POST"])
def setTime():
    if request.method == 'GET':
        longlong = request.args.get('time')
        print longlong
        carCtrl = CarController()
        try:
            carCtrl.setTime(longlong)
            pass
        except Exception as e:
            print e
    return 'Time: ' + longlong
