from telnetlib import test

__author__ = 'Administrator'
import configparser
import time
import os



def ConfigFilePath(PATH):

    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def monkeyConfig(init_file):

    config = configparser.ConfigParser()
    config.read(init_file)
    app = {}
    app["package_name"] = config['DEFAULT']['package_name']
    # mmonkeyconfig.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    app["activity"] = config['DEFAULT']['activity']
    # mac 下使用此句来写log
    LogPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    log = ConfigFilePath(LogPath+'/logFile')+ '/' +time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    #log1 = PATH(LogPath+'/logFile') + '/' +time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    # windows 下
    # log = PATH("../log") + "\\" + time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    app["log"] = log

    app["net"] = config['DEFAULT']['net']
    app["monkey_log"] = log + "monkey.log"
    app["cmd"] = config['DEFAULT']['cmd'] + ">" + app["monkey_log"]
    # mmonkeyconfig.phone_msg_log = mmonkeyconfig.logdir + "\\"
    print(log)
    return app






if __name__=='__main__':
    monkeyConfig()