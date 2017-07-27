__author__ = 'Administrator'
import configparser
import time
import os



PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

FilePath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def monkeyConfig(init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    app = {}
    app["package_name"] = config['DEFAULT']['package_name']
    app["activity"] = config['DEFAULT']['activity']

    # mac 下使用此句来写log
    log = PATH(FilePath+"/logFile") + "/" +time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    # windows 下
    # log = PATH("../log") + "\\" + time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    app["log"] = log

    app["net"] = config['DEFAULT']['net']
    app["monkey_log"] = log + "monkey.log"
    app["cmd"] = config['DEFAULT']['cmd'] + ">" + app["monkey_log"]

    return app

