from datetime import datetime
import sqlalchemy

from .base import metadata


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('email', sqlalchemy.String(120), unique=True, nullable=False),
    sqlalchemy.Column('name', sqlalchemy.String(255)),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean, default=True),
    sqlalchemy.Column('created', sqlalchemy.DateTime, default=datetime.utcnow()),
    sqlalchemy.Column('updated', sqlalchemy.DateTime, default=datetime.utcnow())
) 