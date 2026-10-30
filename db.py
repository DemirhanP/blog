import os
import psycopg
from psycopg.rows import dict_row



def get_conn():
    return psycopg.connect("dbname=blog", row_factory=dict_row)


import os


def get_conn():
    url = os.environ.get("DATABASE_URL", "dbname=blog")
    return psycopg.connect(url, row_factory=dict_row)


def get_conn():
    url = os.environ.get("DATABASE_URL", "dbname=blog")
    return psycopg.connect(url, row_factory=dict_row)