import pymysql
from common.deal_conf import conf

class DealSql:

    def __init__(self):
        self.con = pymysql.connect(host = conf.get('sql','host'),
                              port = eval(conf.get('sql','port')),
                              user = conf.get('sql','user'),
                              password = conf.get('sql','password'),
                              charset = conf.get('sql','charset'),
                              cursorclass = pymysql.cursors.DictCursor
                              )
        self.cur = self.con.cursor()

    def find_one(self,sql):
        '''
        查询一条数据
        :param sql:
        :return:
        '''
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res

    def find_all(self,sql):
        '''
        查询所有数据
        :param sql:
        :return:
        '''
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def get_count(self,sql):
        '''
        获取查询数量
        :param sql:
        :return:
        '''
        self.con.commit()
        res = self.cur.execute(sql)
        return res
