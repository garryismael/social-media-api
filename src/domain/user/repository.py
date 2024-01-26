from abc import ABCMeta, abstractmethod

from src.domain.user.model import User, UserRequestDTO


class UserRepository(metaclass=ABCMeta):

    @abstractmethod
    async def find_all(self) -> list[User]:
        pass

    @abstractmethod
    async def save(self, user_dto: UserRequestDTO) -> User:
        pass
