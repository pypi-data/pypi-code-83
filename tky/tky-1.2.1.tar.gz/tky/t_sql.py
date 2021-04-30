# _*_ coding:utf-8 _*_
"""
常用SQL类集合
\n 目前支持的有：
\n SQL(O_conn/M_conn/set_val/upd_del/clear/close) (SQL类，依赖cx_Oracle/pymysql)
\n Es(read_es) （ES类，依赖elasticsearch）
\n Mysql_db class类，依赖pymysql；(子方法：sel_dict/sel_sql/iud_sql/close/page_mus)
\n @author: 'TangKaiYue'
"""
from .t_jde import null


# SQL数据相关集合
class SQL:
    """
    【SQL数据相关集合】\n
    \n 目前已支持方法：
    \n 1、O_conn | Oracle数据库连接配置(依赖cx_Oracle)
    \n 2、M_conn | Mysql数据库连接配置(依赖pymysql)
    \n 3、set_val | 查询数据表的所有数据/第一条数据
    \n 4、upd_del | 修改/删除/新增数据表的数据
    \n 5、clear | 清空数据表
    \n 6、close | 关闭数据库连接
    """

    # Oracle数据库连接配置
    def O_conn(self: str = 'null', pwd: str = 'null', url: str = 'null'):
        """
        【Oracle数据库连接配置】（依赖cx_Oracle）\n
        :param self: str 用户名；
        :param pwd: str 密码；
        :param url: str 数据库连接(含服务名)；
        :return: 输出数据库连接结果；
        """
        try:
            # 判断必要入参
            if null(self) == 'N' or null(pwd) == 'N' or null(url) == 'N':
                return print("入参异常：连接数据库的 账号、密码、URL 都不能为空...")
            else:
                import cx_Oracle  # 模块引用
                cs = cx_Oracle.connect(str(self), str(pwd), str(url), encoding="UTF-8")
                return cs
        except EnvironmentError as err:
            return '发生异常：%s' % err

    # Mysql数据库连接配置
    def M_conn(self: str = 'null', code: int = '3306', name: str = 'null', pwd: str = 'null', db: str = 'null'):
        """
        【Mysql数据库连接配置】（依赖pymysql）\n
        :param self: str 连接地址/IP；
        :param code: int 端口号，默认3306；
        :param name: str 用户名；
        :param pwd: str 密码；
        :param db: str  数据库名称；
        :return: 输出数据库连接结果；
        """
        try:
            # 判断必要入参
            if null(self) == 'N' or null(name) == 'N' or null(pwd) == 'N' or null(db) == 'N':
                return print("入参异常：连接数据库 地址、用户、密码、库名 都不能为空...")
            import pymysql
            conn = pymysql.connect(host=str(self), port=int(code), user=str(name), passwd=str(pwd), db=str(db),
                                   charset='utf8', autocommit=True)
            return conn
        except EnvironmentError as err:
            return '发生异常：%s' % err

    # 查询数据表的数据(所有/第一条)
    def set_val(self: str = 'null', conn: str = 'null', tp: str = 'all'):
        """
        【查询数据表的数据(所有/第一条)】\n
        使用注意：大量数据查询不建议使用此项功能；\n
        :param self: str sql语句；
        :param conn: str 数据库连接,如：SQL.O_conn()；
        :param tp: str 查询所有/第一条(all/one),默认查全部；
        :return:  输出结果；
        """
        try:
            # 判断必要入参
            if null(conn) == 'N' or null(self) == 'N':
                return "异常：SQL语句、数据库连接值 不能为空！！！（PS:连接值可参考连接方法SQL.O_conn()）"
            # 获取游标
            with conn.cursor() as cursor:
                try:
                    cursor.execute(self)
                except Exception as e:
                    cursor.close()  # 关闭游标
                    return print('发生异常:%s \n传入的SQL：%s; 数据连接：%s' % (e, self, conn))
                if tp == 'all' or tp == 'ALL' or tp == 'All':
                    val = cursor.fetchall()
                    v_list = list(val)
                    return v_list
                if tp == 'one' or tp == 'ONE' or tp == 'One':
                    val = cursor.fetchone()
                    v_list = list(val)
                    return v_list
        except EnvironmentError as err:
            return '发生异常：%s' % err

    # 修改/删除/新增数据表的数据
    def upd_del(self: str = 'null', conn: str = 'null'):
        """
        【修改/删除/新增数据表的数据】\n
        :param self: str sql语句；
        :param conn: str 数据库连接,如：SQL.O_conn()；
        :return:  输出结果；
        """
        try:
            # 判断必要入参
            if null(conn) == 'N' or null(self) == 'N':
                return "异常：SQL语句、数据库连接值 都不能为空！！！（PS:连接值可参考连接方法SQL.O_conn()）"
            # 获取游标
            with conn.cursor() as cursor:
                try:
                    cursor.execute(self)  # 执行SQL
                except Exception as err:
                    conn.rollback()  # 事务回滚（发生错误则回滚）
                    cursor.close()  # 关闭游标
                    return print('传入的SQL：%s; 数据连接：%s \n 执行异常:%s ' % (self, conn, err))
                else:
                    conn.commit()  # 事务提交
                    new_nums = cursor.rowcount
                    return print('执行成功：', new_nums)
        except EnvironmentError as err:
            return '发生异常：%s' % err

    # 清除表数据
    def clear(self: str = 'null', table_name: str = 'null'):
        """
        【修改数据表的数据】\n
        :param self: str 数据库连接,如：SQL.O_conn()；
        :param table_name: str 要清除的数据表名；
        :return:  输出结果；
        """
        if null(table_name) == 'N':
            return "异常：转入的表名为空！"
        real_sql = "delete from " + table_name + ";"
        with self.cursor() as cursor:
            try:
                # 取消表的外键约束
                cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
                cursor.execute(real_sql)
            except Exception as err:
                self.rollback()  # 事务回滚（发生错误则回滚）
                cursor.close()  # 关闭游标
                return print('传入的SQL：%s; \n数据连接：%s \n执行异常:%s ' % (real_sql, self, err))
            else:
                self.commit()  # 事务提交
                new_nums = cursor.rowcount
                return print('清除成功：', new_nums)

    # 关闭数据库
    def close(self):
        """
        :param self: str 数据库连接,如：SQL.O_conn()；
        :return: 无输出，直接关闭数据库连接；
        """
        if null(self) == 'N':
            return "异常：转入的数据库连接为空！"
        self.close()


# ES数据相关集合
class Es:
    """
    【ES数据相关集合】\n
    \n 目前已支持方法：
    \n 1、read_es | 链接ES数据并查询(依赖elasticsearch)
    """

    # 链接ES并查询
    def read_es(self, port, index, querys: str = '{ "query": { "match_all": {} } }'):
        """
        【连接es数据】\n
        :param self: es的host；
        :param port: 连接端口；
        :param index: 索引名；
        :param querys: 查询条件；
        :return: 查询结果
        """
        try:
            if null(self) == 'N' or null(port) == 'N' or null(index) == 'N':
                return print('入参异常：ES的host、端口、索引名 不可为空...')
            from elasticsearch import Elasticsearch, helpers
            url = {"host": self, "port": port, "timeout": 150}
            es = Elasticsearch([url])
            if es.ping():
                print("Successfully connect!")
                query = querys
                res = helpers.scan(es, index=index, scroll="20m", query=query)
                return res
            else:
                print("Failed.....")
                exit()
        except EnvironmentError as err:
            return '发生异常：%s' % err


"""新内容起"""


# Mysql数据库连接配置
class Mysql_db:
    def __init__(self, host_s='localhost', port_s=3306, user_s='root', password_s='root', db_s='new_futures'):
        """
        [数据库链接]\n
        :param host_s: 地址
        :param port_s: 端口
        :param user_s: 账号
        :param password_s: 密码
        :param db_s: 数据库
        """
        import pymysql
        try:
            self.db = pymysql.connect(host=str(host_s), port=int(port_s), user=str(user_s), password=str(password_s),
                                      db=str(db_s), charset='utf8', autocommit=True)
            self.cursor = self.db.cursor()  # 普通的游标对象，默认创建的游标对象
            self.SSCursor = self.db.cursor(cursor=pymysql.cursors.SSCursor)  # 以字典的形式返回操作结果
            self.DictCursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)  # 不缓存游标，主要用于当操作需要返回大量数据的时候
            self.SSDictCursor = self.db.cursor(cursor=pymysql.cursors.SSDictCursor)  # 不缓存游标，将结果以字典的形式进行返回
        except Exception as e:
            print('发生异常：%s ' % e)

    def sel_dict(self, sql):
        """
        [以字典形式返回所有查询结果]\n
        :param sql: 传入的SQL语句
        :return: 输出查询结果(字典形式)
        """
        try:
            self.DictCursor.execute(str(sql))  # 执行SQL
            self.db.commit()  # 事务提交
            v_result = self.DictCursor.fetchall()
            return v_result
        except Exception as e:
            return print('发生异常：%s ' % e)

    def sel_sql(self, sql):
        """
        [以普通形式返回所有查询结果]\n
        :param sql: 传入的SQL语句
        :return: 输出查询结果(普通形式)
        """
        try:
            self.cursor.execute(str(sql))  # 执行SQL
            self.db.commit()  # 事务提交
            v_result = self.cursor.fetchall()
            return v_result
        except Exception as e:
            return print('发生异常：%s ' % e)

    def iud_sql(self, sql):
        """
        [以普通形式返回所有查询结果]\n
        :param sql: 传入的SQL语句
        :return: 错误和影响结果
        """
        try:
            self.cursor.execute(str(sql))  # 执行SQL
        except Exception as err:
            self.db.rollback()  # 事务回滚（发生错误则回滚）
            self.db.close()  # 关闭游标
            return print('传入的SQL：%s; 数据连接：%s \n异常信息：%s ' % (str(sql), self, err))
        else:
            self.db.commit()  # 事务提交
            update_nums = self.cursor.rowcount  # 影响数
            return print('执行成功：%s条' % update_nums)

    def close(self):
        self.db.close()

    # 列表页码及内容查询器
    def page_mus(self, table, order, ordertp='asc', page=1, listnum=10, zd='null', tp='and'):
        """
        [页码及内容查询器]\n
        :param table: 表名
        :param order: 要排序的字段名
        :param ordertp: 排序方式，默认asc
        :param page: 页码数
        :param listnum: 每页的条数
        :param zd: 条件字段及数值
        :param tp: 条件连接，默认and
        :return: page_data(总页数/上下页数) data_val(查询的页面内容) page_list(页码循环数量)
        """
        import math
        global page_num
        global vvv
        # 查询出总条数
        if zd != 'null':
            v = []  # 传入字典处理为list
            for key in zd:
                zc = str(key)
                za = " '" + str(zd[key]) + "'"
                vv = zc + za
                v.append(vv)
            tpp = ' %s ' % str(tp)
            vvv = str(tpp).join(v)  # 拼接查询条件
            list_num = "SELECT count(*) ListCount from %s where %s" % (table, vvv)
            list_nums = Mysql_db.sel_sql(self, list_num)
            self.db.commit()
        else:
            list_num = "SELECT count(*) ListCount from %s" % table
            list_nums = Mysql_db.sel_sql(self, list_num)
            self.db.commit()
        # 计算页码数
        page1 = list_nums[0][0] / listnum  # 计算页码，总条数/页条数
        pages = math.ceil(page1)  # 向前取整
        if page <= pages:
            page_num = page
        if page >= pages:
            page_num = pages
        pg1 = (page_num - 1) * listnum
        if pg1 <= 0:
            pg = 0
        else:
            pg = pg1
        # 输出页码数量list
        page_list = []
        for v in range(1, pages + 1):
            page_list.append(str(v))
        # 判断页码状态
        if pages == 1 and page == 1:
            prev_num = 1
            next_num = 1
        else:
            if page <= 1:
                prev_num = 1
                next_num = page + 1
            else:
                prev_num = page - 1
                next_num = page + 1
            if next_num == pages + 1 or page >= pages:
                next_num = page
        # 输出总页数及上下页码
        page_data = {'pages': pages, 'page': page_num, 'next_num': next_num, 'prev_num': prev_num}
        if zd != 'null':
            set_sql = "select * from {0} where 1=1 and {1} order by {2} {3} limit {4},{5};".format(table, vvv, order, ordertp, pg, listnum)
            data_val = Mysql_db.sel_dict(self, set_sql)
            self.db.commit()
        else:
            set_sql = "select * from {0} where 1=1 order by {1} {2} limit {3},{4};".format(table, order, ordertp, pg, listnum)
            data_val = Mysql_db.sel_dict(self, set_sql)
            self.db.commit()
        return page_data, data_val, page_list
