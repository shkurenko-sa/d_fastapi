from datetime import datetime

from app.database.users import users
from app.repositories.base import BaseRepository
from app.models.user import UserIn, User
from app.utils.sec import PasswordHasher


class UserRepository(BaseRepository):
    
    async def create(self, u: UserIn) -> User:
        user = User(
            name = u.name,
            email = u.email,
            password = PasswordHasher.get_password_hash(u.password),
            is_active = True,
            created = datetime.utcnow(),
            updated = datetime.utcnow()
        )
        query = users.insert().values(**user.dict())
        user.id = await self.database.execute(query)
        return user

    async def update():
        pass

    async def get_by_id(id: int):
        return
    
    async def get_by_email(email: str):
        return