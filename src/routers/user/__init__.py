from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.config.container import Container
from src.domain.user.model import UserRequestDTO, UserResponseDTO
from src.domain.user.use_case import CreateUserUseCase, GetUsersUseCase

user_router = APIRouter()


@user_router.post("/users", tags=["users"])
@inject
async def create_user(
    request: UserRequestDTO,
    use_case: CreateUserUseCase = Depends(
        Provide[Container.create_user_use_case])
) -> UserResponseDTO:
    return await use_case.execute(request.dto())


@user_router.get("/users", tags=["users"])
@inject
async def get_users(use_case: GetUsersUseCase = Depends(
    Provide[Container.get_users_use_case])) -> list[UserResponseDTO]:
    return await use_case.execute()
