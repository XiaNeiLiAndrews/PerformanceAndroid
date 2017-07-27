import time,os

import datetime

from PerformanceAndroid.base import AdbCommon
from PerformanceAndroid.base import BaseMonitor
from PerformanceAndroid.base import BaseMonkeyConfig




def add_ini(ini_fileName):


    # adb连接手机
    AdbCommon.AndroidDebugBridge()
    BaseMonkeyConfig.monkeyConfig(PATH(ini_fileName))
    # 打开想要的activity
    ba.open_app(mc["package_name"], mc["activity"])
    temp = ""
    # monkey开始测试
    start_monkey(mc["cmd"], mc["log"])
    time.sleep(1)
    starttime = datetime.datetime.now()

    while True:
        with open(mc["monkey_log"], encoding='utf-8') as monkeylog:
            BaseMonitor.get_cpu(mc["package_name"])
            BaseMonitor.get_men(mc["package_name"])
            BaseMonitor.get_fps(mc["package_name"])
            BaseMonitor.get_battery()
            BaseMonitor.get_flow(mc["package_name"], mc["net"])
            time.sleep(1)  # 每1秒采集检查一次
            if monkeylog.read().count('Monkey finished') > 0:
                endtime = datetime.datetime.now()

                print("测试完成")
                app = {"beforeBattery": BaseMonitor.get_battery(), "net": mc["net"], "monkey_log": mc["monkey_log"]}
                report(app, str((endtime - starttime).seconds) + "秒")
                bo.close()
                break
