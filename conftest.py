import pytest
import os
import requests
import jsonpath
from common.deal_excel import DealExcel
from common.deal_path import DealPath
from common.deal_conf import conf
from common.deal_common import StoreData


@pytest.fixture(scope='class')
def write_results():
    results = []
    yield results

    de = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'register')
    #将执行结果转换成字典
    de.write_all_excel(dict(enumerate(results)))

@pytest.fixture(scope='class')
def write_results_log():
    results = []
    yield results

    de = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'login')
    #将执行结果转换成字典
    de.write_all_excel(dict(enumerate(results)))

@pytest.fixture(scope='class')
def write_results_add():
    results = []
    url = conf.get('env','base_url') + '/member/login'
    #datas ='{"mobile_phone":"{}","pwd":"12345678"}'.format(getattr(StoreData,'user_phone'))
    datas = '{"mobile_phone":"' + getattr(StoreData,'user_phone') + '","pwd":"12345678"}'
    datas = eval(datas)
    headers = eval(conf.get('env','headers2'))
    #调登陆接口
    res = requests.request(method='post',url=url,json = datas,headers = headers).json()

    #cls.member_id = jsonpath.jsonpath(res,'$..id')[0]
    #print(cls.member_id,type(cls.member_id))
    token = "Bearer " + jsonpath.jsonpath(res,"$..token")[0]
    yield results,token

    de = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'add')
    #将执行结果转换成字典
    de.write_all_excel(dict(enumerate(results)))