import sqlite3

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['database'],
            detect_types=sqlite3.PARSE_DECLTYPES
        }
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    dp = g.pop('db', None)

    if db is nor None:
        db.close()
