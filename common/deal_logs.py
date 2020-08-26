import logging
import os
from common.deal_conf import conf
from common.deal_path import DealPath

class DealLogs:

    def myLoger(self):

        #创建日志收集器
        my_logger =  logging.getLogger('zcg')
        my_logger.setLevel(conf.get('log','level'))

        #创建工作台输出流
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log','sh_level'))
        my_logger.addHandler(sh)

        #创建文件输出流
        fh = logging.FileHandler(os.path.join(DealPath().LOG_PATH,'logs.log'),encoding="utf-8")
        fh.setLevel(conf.get('log','fh_level'))
        my_logger.addHandler(fh)

        #设置输出格式
        formats = "%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
        #添加输出格式
        fm = logging.Formatter(formats)
        #将输出格式添加到输出渠道
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return my_logger

myLog = DealLogs().myLoger()


