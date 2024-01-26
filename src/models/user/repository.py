from src.domain.user.model import User, UserRequestDTO
from src.domain.user.repository import UserRepository
from src.models.user import UserModelMapper


class UserRepositoryImpl(UserRepository):

    async def save(self, user_dto: UserRequestDTO) -> User:
        user_db = UserModelMapper(first_name=user_dto.first_name,
                                  last_name=user_dto.last_name,
                                  password=user_dto.password)
        await user_db.save()
        return user_db.cast()

    async def find_all(self) -> list[User]:
        users_db = await UserModelMapper.all()
        users = [user.cast() for user in users_db]
        return users
