from common.deal_excel import DealExcel
from common.deal_path import DealPath
from common.deal_conf import conf
from common.deal_common import DealComm,StoreData
from common.deal_sql import DealSql
import pytest
import os
from requests import request

class TestAdd():

    test_cases = DealExcel(os.path.join(DealPath().DATA_PATH,'cases.xlsx'),'add').read_excel()
    ds = DealSql()

    @pytest.mark.parametrize('cases',test_cases)
    def test_add(self,cases,write_results_add):
        #准备测试数据
        results,token = write_results_add
        method = cases['method']
        url = conf.get('env','base_url') + cases['url']
        # if '#member_id#' in cases['data']:
        #     cases['data'] = cases['data'].replace('#member_id#',str(self.hl.user_id))
        cases['data'] = DealComm().repalce_string(cases['data'])
        test_datas = eval(cases['data'])
        headers = eval(conf.get('env','headers2'))
        cases_id = cases['case_id'] + 1
        headers['Authorization'] = token
        #headers['Authorization'] = getattr(StoreData,'token')
        expected = eval(cases['expected'])

        #调用请求
        try:
            res = request(method=method,url=url,json=test_datas,headers=headers).json()

            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
            if cases['query_sql']:
                # sql = cases['query_sql'].format(self.hl.user_id)
                sql = DealComm().repalce_string(cases['query_sql'])
                count = self.hm.count(sql)
                self.assertEqual(1,count)
                # sql_res = self.hm.find_one(sql)
                # setattr(StoreData,'pass_loin')

            results = "测试通过"

        except AssertionError as e:

            results = "测试不通过"
            raise e

        except Exception as e:
            results = "接口异常"

        finally:
            #记录测试结果
            myLog.error("测试案例：==={}==={}".format(cases['title'],results))
            self.he.write_excel(row=cases_id,col=8,text=results)

