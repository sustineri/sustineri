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
        sql = '''
            SELECT i.gwp, r.upload_week, u.user_id
            FROM items i, receipts r, users u
            WHERE u.user_id = r.user_id AND r.receipt_id = i.receipt_id
            GROUP BY r.upload_week
        '''
        cursor = conn.cursor()
        cursor.execute(sql)

        data_all_users = {}
        data_our_user = {}
        for upload_week in cursor:
            per_week_all_users = []
            per_week_our_user = []
            for gwp, user_id in upload_week:
                per_week_all_users.add(gwp)
                if user_id is 1:
                    per_week_our_user.add(gwp)

            len_all = len(per_week_all_users)
            if len_all > 0:
                data_all_users[upload_week] = sum(per_week_all_users) / len_all
            else:
                data_all_users[upload_week] = 0

            len_our = len(per_week_our_user)
            if len_our > 0:
                data_our_user[upload_week] = sum(per_week_our_user) / len_our
            else:
                data_our_user[upload_week] = 0

        data = []
        for key in data_all_users:
            record = {}
            record['date'] = key
            record['gwp'] = data_all_users[key]
            record['avg'] = data_our_user[key]
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
        sql = '''
            INSERT INTO receipts (upload_date, user_id)
            VALUES (WEEKOFYEAR(CURDATE()), 1);
            INSERT INTO items (name, price, amount, gwp, receipt_id)
            VALUES (%s, %s, %s, %s, LAST_INSERT_ID());
        '''
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, items);
            cursor.commit()
        except:
            cursor.rollback()
