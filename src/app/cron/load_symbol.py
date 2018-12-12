#!/usr/bin/env python3.6

import requests
import MySQLdb
import uuid

def do_load():
    res = requests.get("https://api.fcoin.com/v2/public/symbols")
    data = res.json()["data"]

    db = MySQLdb.connect("127.0.0.1", "root", "123456", "qos", charset='utf8' )
    cursor = db.cursor()
    insert_template = "insert into app_symbol (id, name, base_currency, quote_currency, price_decimal, amount_decimal, created_at, updated_at) values ('%s', '%s', '%s', '%s', %s,  %s, %s, %s)"
    update_template = "update app_symbol set price_decimal=%s, amount_decimal=%s, updated_at=%s where name='%s'"

    for i in data:
        try:
            sql = insert_template % (str(uuid.uuid4()).replace("-", ""), i['name'], i['base_currency'], i['quote_currency'], i['price_decimal'], i['amount_decimal'], 'now()', 'now()');
            cursor.execute(sql)
        except MySQLdb.IntegrityError:
            sql = update_template % (i['price_decimal'], i['amount_decimal'], 'now()', i['name']);
            cursor.execute(sql)
        # print(sql)
       
    db.commit()
    db.close()

def main():
    do_load()


if __name__ == '__main__':
    main()
