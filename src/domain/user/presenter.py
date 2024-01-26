from abc import ABCMeta, abstractmethod

from src.domain.user.model import UserResponseDTO


class UserPresenter(metaclass=ABCMeta):

    @abstractmethod
    def prepare_view(self, data: UserResponseDTO) -> UserResponseDTO:
        pass

    @abstractmethod
    def prepare_list_view(self, data: list[UserResponseDTO]) -> list[UserResponseDTO]:
        pass
