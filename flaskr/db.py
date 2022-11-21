import sqlite3
import json
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    l=[]
    for i in range (1,61):
        l.append(i)
    s=json.dumps(l)
    current_app.logger.info("generated seats: %s", s)
    db.execute('UPDATE movies SET seats = ?', (s,))
    db.commit()

def init_app(app):
    app.teardown_appcontext(close_db)