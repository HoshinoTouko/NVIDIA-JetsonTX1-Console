from Modules.mode import Mode

from Modules.CarController import CarController
from flask import Blueprint, session, request, render_template, redirect, url_for

CTRL = Blueprint('ctrl', __name__)
carController = CarController()

@CTRL.route('/get_distance/front')
def get_distance_front():
    front, back = carController.readDistance()
    result =  front
    return str(result)

@CTRL.route('/get_distance/back')
def get_distance_back():
    front, back = carController.readDistance()
    result =  back
    return str(result)

@CTRL.route('/change_mode/<moduleId>')
def change_mode(moduleId):
    Mode.changeMode(moduleId)
    return 'Change to ' + moduleId

@CTRL.route('/go')
def go():
    carController.go()
    return '1'

@CTRL.route('/back')
def back():
    carController.back()
    return '1'

@CTRL.route('/stop')
def stop():
    carController.stop()
    return '1'

@CTRL.route('/left')
def left():
    carController.left_turn()
    return '1'

@CTRL.route('/right')
def right():
    carController.right_turn()
    return '1'

@CTRL.route('/left_ahead')
def left_ahead():
    carController.turn_left_ahead()
    return '1'

@CTRL.route('/right_ahead')
def right_ahead():
    carController.turn_right_ahead()
    return '1'

@CTRL.route('/left_turn')
def left_turn():
    carController.turn_left()
    return '1'

@CTRL.route('/right_turn')
def right_turn():
    carController.turn_right()
    return '1'


@CTRL.route('/left_back_turn')
def left_back_turn():
    carController.turn_back_left()
    return '1'

@CTRL.route('/right_back_turn')
def right_back_turn():
    carController.turn_back_right()
    return '1'

@CTRL.route('/speed_up')
def speed_up():
    carController.speed_up()
    return '1'
