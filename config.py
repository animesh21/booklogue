import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:user@localhost/booklogue'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db.repository')
