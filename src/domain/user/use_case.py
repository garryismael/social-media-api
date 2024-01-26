from abc import ABCMeta, abstractmethod

from src.domain.user.model import UserRequestDTO, UserResponseDTO
from src.domain.user.presenter import UserPresenter
from src.domain.user.repository import UserRepository


class CreateUserUseCase(metaclass=ABCMeta):

    @abstractmethod
    async def execute(self, dto: UserRequestDTO) -> UserResponseDTO:
        pass


class CreateUserInteractor(CreateUserUseCase):

    def __init__(self, user_repository: UserRepository, user_presenter: UserPresenter) -> None:
        self.user_repository = user_repository
        self.user_presenter = user_presenter
        
    async def execute(self, dto: UserRequestDTO) -> UserResponseDTO:
        user = await self.user_repository.save(dto)
        return user

class GetUsersUseCase(metaclass=ABCMeta):

    @abstractmethod
    async def execute(self) -> list[UserResponseDTO]:
        pass


class GerUsersInteractor(GetUsersUseCase):

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def execute(self) -> list[UserResponseDTO]:
        return await self.user_repository.find_all()
