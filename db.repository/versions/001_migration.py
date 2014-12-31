from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
book_picture = Table('book_picture', pre_meta,
    Column('width', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('height', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('mimetype', VARCHAR(length=255), nullable=False),
    Column('original', TINYINT(display_width=1), nullable=False),
    Column('created_at', DATETIME, nullable=False),
    Column('book_id', INTEGER(display_width=11), primary_key=True, nullable=False),
)

book = Table('book', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=150), nullable=False),
    Column('category_id', Integer),
    Column('description', Text),
    Column('rating', Float),
    Column('isbn', String(length=15)),
    Column('picture', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['book_picture'].drop()
    post_meta.tables['book'].columns['picture'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['book_picture'].create()
    post_meta.tables['book'].columns['picture'].drop()
