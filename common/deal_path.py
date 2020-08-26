import os

class DealPath:

    #项目绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #案例路径
    CASE_PATH = os.path.join(BASE_PATH,'cases')

    #测试数据
    DATA_PATH = os.path.join(BASE_PATH,'datas')

    #配置路径
    CONF_PATH = os.path.join(BASE_PATH,'conf')

    #日志路径
    LOG_PATH = os.path.join(BASE_PATH,r'results\logs')

    #报告路径
    REPORT_PATH = os.path.join(BASE_PATH,r'results\reports')


if __name__ == '__main__':
    pt = DealPath.BASE_PATH

    print(pt)