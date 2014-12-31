from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
book_category = Table('book_category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('book_id', Integer),
    Column('category_id', Integer),
)

book = Table('book', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('title', VARCHAR(length=150), nullable=False),
    Column('category_id', INTEGER(display_width=11)),
    Column('description', TEXT),
    Column('rating', FLOAT),
    Column('isbn', VARCHAR(length=15)),
    Column('picture', VARCHAR(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['book_category'].create()
    pre_meta.tables['book'].columns['category_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['book_category'].drop()
    pre_meta.tables['book'].columns['category_id'].create()
