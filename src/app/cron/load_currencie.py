#!/usr/bin/env python3.6

import requests
import MySQLdb
import uuid

res = requests.get("https://api.fcoin.com/v2/public/currencies")
data = res.json()["data"]


def do_load():
    db = MySQLdb.connect("127.0.0.1", "root", "123456", "qos", charset='utf8' )
    cursor = db.cursor()
    sql_template = "insert into app_currencie (id, name, created_at, updated_at) values ('%s', '%s', %s, %s)"

    sql = "delete from app_currencie"
    cursor.execute(sql)
    db.commit()

    for i in data:
        try:
            sql = sql_template % (str(uuid.uuid4()).replace("-", ""), i, 'now()', 'now()');
            cursor.execute(sql)
        except MySQLdb.IntegrityError:
            pass
        # print(sql)

    db.commit()
    db.close()


def main():
    do_load()


if __name__ == '__main__':
    main()
