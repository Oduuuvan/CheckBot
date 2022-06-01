__all__ = ['DB']

from bot.config import DB_PASS
from bot.db.database import Database

DB = Database(DB_PASS)
DB.create_tables()
