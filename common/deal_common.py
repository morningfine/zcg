import re
from common.deal_conf import conf
from common.deal_sql import DealSql
import random
class StoreData:
    pass

class DealComm:

    def create_phone(self):
        '''
        创建随机手机号
        :return:
        '''
        ds = DealSql()
        while True:
            rd = str(random.random())
            rd = rd[2:10]
            res = '138'+rd
            sql = 'select * from futureloan.member WHERE mobile_phone="{}";'.format(res)
            if ds.get_count(sql) == 0:
                break
        return res

    def repalce_string(self,str):
        """
        替换字符串
        :param str:
        :return:
        """

        while re.search('#(.*?)#',string=str):
            res = re.search('#(.*?)#',string=str)

            #提取值
            item = res.group()
            #提取（）中的值
            value = res.group(1)

            try:
                str = str.replace(item,conf.get('test_data',value))
            except:
                str = str.replace(item,getattr(StoreData,value))

        return str

        '''
        fa = re.findall('#(.*?)#',string=str)
        for item in fa:

            str.replace(fa,)
'''

if __name__ == '__main__':
    cp = DealComm().create_phone()
    print(cp)