from configparser import RawConfigParser
from common.deal_path import DealPath
import os
class DealConf(RawConfigParser):

    def read_conf(self):
        path = os.path.join(DealPath().CONF_PATH,'config.ini')
        rd = RawConfigParser()
        rd.read(path,encoding='utf-8')

        return rd

conf = DealConf().read_conf()