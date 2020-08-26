from common.deal_excel import DealExcel
from common.deal_path import DealPath
from common.deal_conf import conf
from common.deal_common import DealComm,StoreData
from common.deal_sql import DealSql
import pytest
import os
from requests import request

class TestRegister:
    test_cases = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'register').read_excel()
    ds = DealSql()

    @pytest.mark.parametrize('case',test_cases)
    def test_register(self,case,write_results):
        rs = write_results

        phone = DealComm().create_phone()
        setattr(StoreData,'phone',phone)

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
                if case['query_sql']:
                    case['query_sql'] = DealComm().repalce_string(case['query_sql'])
                    res = self.ds.get_count(case['query_sql'])
                    sql_res = self.ds.find_one(case['query_sql'])
                    assert res == 1
                    if '管理员用户' in case['title']:
                        setattr(StoreData,'admin_phone',phone)
                    elif '普通用户' in case['title']:
                        setattr(StoreData,'user_phone',phone)
                    setattr(StoreData,'member_id',str(sql_res['id']))
            except AssertionError as e:
                rs.append('测试不通过new')
                raise e
            else:
                rs.append('测试通过new')