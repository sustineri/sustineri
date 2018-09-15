from os import environ
from os.path import abspath, dirname, join

import MySQLdb as mariadb

CURRENT_PATH = abspath(dirname(abspath(__file__)))


class DatabaseInitialiser:

    @staticmethod
    def init():
        conn = mariadb.connect(
            host=environ.get('DATABASE_HOST'),
            port=int(environ.get('DATABASE_PORT')),
            user=environ.get('DATABASE_USER'),
            passwd=environ.get('DATABASE_PASSWORD'),
            db=environ.get('DATABASE_NAME')
        )
        cursor = conn.cursor()
        for statement in open(join(CURRENT_PATH, 'init.sql')).readlines():
            cursor.execute(statement)
