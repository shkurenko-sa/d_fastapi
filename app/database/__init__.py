from .base import metadata, engine
from app.database.users import users


metadata.create_all(bind=engine)
