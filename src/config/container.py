from dependency_injector import containers, providers

from src.domain.user.use_case import CreateUserInteractor, GerUsersInteractor
from src.models.user.repository import UserRepositoryImpl
from src.routers.presenter import UserPresenterImpl


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["src.routers.user"])
    config = providers.Configuration(yaml_files=["config.yml"])

    # repositories
    user_repository = providers.Factory(UserRepositoryImpl)

    # presenters
    user_presenter = providers.Factory(UserPresenterImpl)

    # use cases
    create_user_use_case = providers.Factory(CreateUserInteractor,
                                             user_repository=user_repository)
    get_users_use_case = providers.Factory(GerUsersInteractor,
                                           user_repository=user_repository)
