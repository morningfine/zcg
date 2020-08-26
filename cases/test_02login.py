from common.deal_excel import DealExcel
from common.deal_path import DealPath
from common.deal_conf import conf
from common.deal_common import DealComm,StoreData
from common.deal_sql import DealSql
import pytest
import os
from requests import request
from jsonpath import jsonpath

class TestLogin:
    test_cases = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'login').read_excel()
    ds = DealSql()

    @pytest.mark.parametrize('case',test_cases)
    def test_login(self,case,write_results_log):
        rs = write_results_log

        headers = eval(conf.get('env','headers2'))
        method = case['method']
        url = conf.get('url','base_url') + case['url']
        case['data'] =  DealComm().repalce_string(case['data'])
        data = eval(case['data'])
        expect = eval(case['expected'])

        try:
            if method == 'get' or method == 'GET':
                results = request(method=method,url=url,data=data,headers=headers)
            else:
                results = request(method=method,url=url,json=data,headers=headers)
        except Exception as e:
            rs.append('请求异常new')
            assert '请求异常' == '0'
        else:
            result = results.json()
            print(result)

            try:
                #assert (results.status_code,result['code'],result['msg']) == (200,expect['code'],expect['msg'])
                assert results.status_code == 200
                assert result['code'] == expect['code']
                assert result['msg'] == expect['msg']
                if jsonpath(result,'$..token'):
                    if '管理员' in case['title']:
                        setattr(StoreData,'admin_token','Bearer '+ jsonpath(result,'$..token')[0])
                        setattr(StoreData,'admin_member_id',str(jsonpath(result,'$..id')[0]))
                    elif '普通用户' in case['title']:
                        setattr(StoreData,'user_token','Bearer '+ jsonpath(result,'$..token')[0])
                        setattr(StoreData,'user_member_id',str(jsonpath(result,'$..id')[0]))

            except AssertionError as e:
                rs.append('测试不通过new')
                raise e
            else:
                rs.append('测试通过new')
