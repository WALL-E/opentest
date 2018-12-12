#!/usr/bin/env python3.6
import sys

import requests
import MySQLdb
import uuid
import fcoin

def do_load():
    db = MySQLdb.connect("127.0.0.1", "root", "123456", "qos", charset='utf8' )
    cursor = db.cursor()

    sql = "select a.key, a.secret from app_certification a, app_account b where a.id = b.certification_id order by b.updated_at limit 1"
    cursor.execute(sql)
    key, secret = cursor.fetchone()
    api = fcoin.authorize(key, secret)
    data = api.get_balance()["data"]

    insert_template = "insert into app_balance (id, currency, category, available, frozen, balance, created_at, updated_at) values ('%s', '%s', '%s', %s, %s,  %s, %s, %s)"
    update_template = "update app_balance set available=%s, frozen=%s, balance=%s, updated_at=%s where currency='%s' and category='%s'"

    for i in data:
        try:
            sql = insert_template % (str(uuid.uuid4()).replace("-", ""), i['currency'], i['category'], i['available'], i['frozen'], i['balance'], 'now()', 'now()');
            cursor.execute(sql)
        except MySQLdb.IntegrityError:
            sql = update_template % (i['available'], i['frozen'], i['balance'], 'now()', i['currency'], i['category']);
            cursor.execute(sql)
        # print(sql)
      

    db.commit()
    db.close()


def main():
    do_load()


if __name__ == '__main__':
    main()
