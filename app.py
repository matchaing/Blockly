# from crypt import methods
import subprocess
import threading
from time import sleep
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import logging
import json
import os
import signal
from tello import Tello
from pymongo import MongoClient
import sys


# flask 객체 인스턴스 생성
app = Flask(__name__)
CORS(app)

tello = Tello()  # 객체 생성. 소켓 연결 됨
connection_bool = False
output = ''

# logger 생성
logger = logging.getLogger('log_test')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s -" u"%(message)s")
# max_byte = 10 * 1024

fileHandler_debug = logging.FileHandler('debug.log')
fileHandler_debug.setLevel(logging.DEBUG)
fileHandler_debug.setFormatter(formatter)

fileHandler_warning = logging.FileHandler('warning.log')
fileHandler_warning.setLevel(logging.WARNING)
fileHandler_warning.setFormatter(formatter)

logger.addHandler(fileHandler_debug)
logger.addHandler(fileHandler_warning)

# 메모용 - 위에서부터 순서대로 위험도가 5 -> 1단계
# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")


@ app.route("/", methods=['GET', 'POST'])
def test():
    res = request.args.get('id')
    print(request.method, res)
    global connection_bool
    if request.method == 'GET':
        if request.args.get('id') == 'connect':
            connection_bool = True
            connection_string = connection()
            connection_string = '연결되었습니다.'
            return connection_string

        elif request.args.get('id') == 'disconnect':
            os.kill(os.getpid(), signal.SIGINT)
            # disconnection()
            # tello.on_close()
            # tello.send_command('land')

        elif request.args.get('id') == 'battery':
            battery = get_battery().strip()
            return battery

    elif request.method == 'POST':
        if connection_bool:
            params = request.get_json()
            if params is None or params == {}:
                print('오류')
            else:
                json_obj = json.dumps(params)
                json_parse(json_obj)

    return render_template('index.html')


def connection():
    # 연결 된 텔로에 'command' 명령 보냄
    tello.send_command('command')  # Enter SDK Mode, 전송된 바이트 수를 리턴(command:7)
    response = tello.response.decode('utf-8')
    # response = 'ok'
    if response == 'ok':
        connection_string = '연결되었습니다.'
        print(connection_string)
    else:
        connection_string = '연결 오류 '
        print(connection_string + str(response))
        logger.error(connection_string + str(response))
    return connection_string


# def disconnection():
#     tello.send_command('command')  # Enter SDK Mode, 전송된 바이트 수를 리턴(command:7)
#     #response, ip = g.socket.recvfrom(1024)
#     response = 'ok'
#     if response == 'ok':
#         print('연결 해제')
#         os.kill(os.getpid(), signal.SIGINT)
#     else:
#         print('연결 해제 오류 :', response)

def get_battery():
    tello.send_command('battery?')
    current_battery = tello.response.decode('utf-8')
    # current_battery = str(60)
    return current_battery


# @ app.route('/mongo', methods=['POST'])
# def mongoTest():
#     client = MongoClient('mongodb://localhost:127.0.0.1/')
#     db = client.newDatabase
#     collection = db.mongoTest
#     results = collection.find()
#     client.close()
#     return render_template("index.html", data=results)

# @app.route('/update', methods=['POST'])
# def update():
#     return jsonify({
#         'output': output,
#     })



def returnCommand(text):
    return text

def list_to_int(li):
    for word in li:
        return int(word)

def get_build_version():
	out = subprocess.Popen('ls -al', shell=True, stdout=subprocess.PIPE).stdout 
	return out.readline()


def list_save(li):
    string = ''
    for word in li:
        string += str(word) + ' '
    return string


# if 문
def json_blocks_if(jsonArray):
    print(jsonArray.get("inputs").get("IF0").get("block").get("fields"))

    params = jsonArray.get("inputs").get("IF0").get("block").get("type")

    if params == "logic_compare":   # 비교
        print(jsonArray.get("inputs").get("IF0").get("block").get(
            "inputs").get("A").get("block").get("fields"))
        print(jsonArray.get("inputs").get("IF0").get("block").get(
            "inputs").get("B").get("block").get("fields"))

    if params == "logic_negate":  # not
        print(jsonArray.get("inputs").get("IF0").get("block").get(
            "inputs").get("BOOL").get("block").get("fields"))
    if not(jsonArray.get("inputs").get("DO")):
        print("")
    else:
        json_blocks_parse(jsonArray.get("inputs").get("DO"))


# for 문
def json_blocks_for(jsonArray):
    name = jsonArray.get('type')
    value = list(jsonArray.get("inputs").get(
        "TIMES").get("block").get("fields").values())

    num = list_to_int(value)
    print(name, num)  # 드론에 안 보내도 됨
    if jsonArray.get("inputs").get("DO") is not None:
        for i in range(int(num)):
            json_blocks_parse(jsonArray.get("inputs").get("DO"))
        print("")


def wait(sec):
    print("Wait ", sec, "sec")
    sleep(int(sec))


# 일반 블럭
def json_blocks_parse(data):

    jsonArray = data.get("block")
    name = jsonArray.get("type")
    if jsonArray.get("type") == "controls_repeat_ext":
        json_blocks_for(jsonArray)
        command = ''
    elif jsonArray.get("type") == "controls_if":
        json_blocks_if(jsonArray)
    elif jsonArray.get("type") == "flight_move":
        command = list_save(list(jsonArray.get("fields").values()))
        print(command)
        tello.send_command(command)
    elif jsonArray.get("type") == "wait":
        command = ''
        val = list_save(list(jsonArray.get("fields").values()))
        wait(val)
    else:
        if jsonArray.get("fields") is not None:
            val = list_save(list(jsonArray.get("fields").values()))
            command = name + ' ' + val
        else:
            command = name

        # tello.send_command(command)
        print(command)
        output = command
        if command != '':
            tello.send_command(command)

    if jsonArray.get("next") is not None:
        json_blocks_parse(jsonArray.get("next"))


def json_parse(data):
    jsonObject = json.loads(data)
    jsonArray = jsonObject.get("blocks").get('blocks')
    for word in jsonArray:
        if word.get("type") == "controls_repeat_ext":
            json_blocks_for(word)
            print("")
            command = ''
        elif word.get("type") == "controls_if":
            json_blocks_if(word)
        elif word.get("type") == "flight_move":
            command = list_save(list(word.get("fields").values()))
        elif word.get("type") == "wait":
            command = ''
            val = list_save(list(word.get("fields").values()))
            wait(val)
        else:
            if word.get("fields") is not None:
                val = list_save(list(word.get("fields").values()))
                command = word.get('type') + ' ' + val
            else:
                command = word.get('type')

        print(command)
        output = command
        if command != '':
            tello.send_command(command)

        if word.get("next") is not None:
            json_blocks_parse(word.get("next"))
        print("")


if __name__ == "__main__":
    app.run()