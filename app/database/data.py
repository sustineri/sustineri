from os import environ
from os.path import abspath, dirname, join

import MySQLdb as mariadb

CURRENT_PATH = abspath(dirname(abspath(__file__)))


class SustineriData:

    @staticmethod
    def get_overview():
        conn = mariadb.connect(
            host=environ.get('DATABASE_HOST'),
            port=int(environ.get('DATABASE_PORT')),
            user=environ.get('DATABASE_USER'),
            passwd=environ.get('DATABASE_PASSWORD'),
            db=environ.get('DATABASE_NAME')
        )
        sql_all = '''
            SELECT AVG(i.gwp), r.upload_week
            FROM items i, receipts r
            WHERE r.receipt_id = i.receipt_id
            GROUP BY r.upload_week
        '''
        sql_single = '''
            SELECT AVG(i.gwp), r.upload_week
            FROM items i, receipts r
            WHERE r.user_id = 1 AND r.receipt_id = i.receipt_id
            GROUP BY r.upload_week
        '''
        cursor = conn.cursor()
        cursor.execute(sql_all)

        data_all = {}
        for gwp, upload_week in cursor:
            data_all[upload_week] = gwp

        cursor.execute(sql_single)

        data_single = {}
        for gwp, upload_week in cursor:
            data_single[upload_week] = gwp

        data = []
        keys = set(list(data_all.keys()) + list(data_single.keys()))
        for key in keys:
            record = {}
            record['date'] = key

            if key in data_all:
                record['avg'] = float(data_all[key])
            else:
                record['avg'] = 0

            if key in data_single:
                record['gwp'] = float(data_single[key])
            else:
                record['gwp'] = 0

            data.append(record)

        return data


    def add_items(items):
        conn = mariadb.connect(
            host=environ.get('DATABASE_HOST'),
            port=int(environ.get('DATABASE_PORT')),
            user=environ.get('DATABASE_USER'),
            passwd=environ.get('DATABASE_PASSWORD'),
            db=environ.get('DATABASE_NAME')
        )
        sql_receipt = '''
            INSERT INTO receipts (upload_week, user_id)
            VALUES (WEEKOFYEAR(CURDATE()), 1);
        '''
        sql_items = '''
            INSERT INTO items (name, price, amount, gwp, receipt_id)
            VALUES (%s, %s, %s, %s, %s);
        '''
        cursor = conn.cursor()
        try:
            cursor.execute(sql_receipt)
            items_receipt = list(map(lambda x: x + (cursor.lastrowid, ), items))
            cursor.executemany(sql_items, items_receipt)
            conn.commit()
        except:
            cursor.rollback()
