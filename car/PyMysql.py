import MySQLdb
import MySQLdb.cursors

STORE_RESULT_MODE = 0
USE_RESULT_MODE = 1

CURSOR_MODE = 0
DICTCURSOR_MODE = 1
SSCURSOR_MODE = 2
SSDICTCURSOR_MODE = 3

FETCH_ONE = 0
FETCH_MANY = 1
FETCH_ALL = 2


class PyMysql:
    def __init__(self):
        self.conn = None
        pass

    def newConnection(self, host, user, passwd, defaultdb):

        self.conn = MySQLdb.Connect(host, user, passwd, defaultdb)
        if self.conn.open == False:
            raise None

    def closeConnnection(self):

        self.conn.close()

    def query(self, sqltext, mode=STORE_RESULT_MODE):

        if self.conn == None or self.conn.open == False:
            return -1
        self.conn.query(sqltext)
        if mode == 0:
            result = self.conn.store_result()
        elif mode == 1:
            result = self.conn.use_result()
        else:
            raise Exception("mode value is wrong.")
        return (self.conn.affected_rows(), result)

    def fetch_queryresult(self, result, maxrows=1, how=0, moreinfo=False):

        if result == None: return None
        dataset = result.fetch_row(maxrows, how)
        if moreinfo is False:
            return dataset
        else:
            num_fields = result.num_fields()
            num_rows = result.num_rows()
            field_flags = result.field_flags()
            info = (num_fields, num_rows, field_flags)
            return (dataset, info)

    def execute(self, sqltext, args=None, mode=CURSOR_MODE, many=False):

        if mode == CURSOR_MODE:
            curclass = MySQLdb.cursors.Cursor
        elif mode == DICTCURSOR_MODE:
            curclass = MySQLdb.cursors.DictCursor
        elif mode == SSCURSOR_MODE:
            curclass = MySQLdb.cursors.SSCursor
        elif mode == SSDICTCURSOR_MODE:
            curclass = MySQLdb.cursors.SSDictCursor
        else:
            raise Exception("mode value is wrong")

        cur = self.conn.cursor(cursorclass=curclass)
        line = 0
        if many == False:
            if args == None:
                line = cur.execute(sqltext)
            else:
                line = cur.execute(sqltext, args)
        else:
            if args == None:
                line = cur.executemany(sqltext)
            else:
                line = cur.executemany(sqltext, args)
        self.conn.commit()
        return (line, cur)

    def fetch_executeresult(self, cursor, mode=FETCH_ONE, rows=1):

        if cursor == None:
            return
        if mode == FETCH_ONE:
            return cursor.fetchone()
        elif mode == FETCH_MANY:
            return cursor.fetchmany(rows)
        elif mode == FETCH_ALL:
            return cursor.fetchall()


if __name__ == "__main__":
    print help(PyMysql)
