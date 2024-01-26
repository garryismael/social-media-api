
from src.domain.user.model import UserResponseDTO
from src.domain.user.presenter import UserPresenter


class UserPresenterImpl(UserPresenter):

    def prepare_view(self, data: UserResponseDTO) -> UserResponseDTO:
        return data

    def prepare_list_view(self, data: list[UserResponseDTO]) -> list[UserResponseDTO]:
        return data
