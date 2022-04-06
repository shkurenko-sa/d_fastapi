from databases import Database
import sqlalchemy

from app.config import DB


DATABASE_URL = f"postgresql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['db']}"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)