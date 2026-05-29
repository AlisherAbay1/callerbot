from dishka import Provider, Scope, provide
from src.app.infrastructure.database.repositories import UserRepository
from src.app.application.interfaces import UserRepositoryProtocol
from src.app.application.interactors.private import (
    StartInteractor,
    RegisterUserGlobalyInteractor,
    UnRegisterUserGlobalyInteractor,
    SetEmojiGlobalyInteractor,
)


class PrivateProvider(Provider):
    scope = Scope.REQUEST
    user_repository = provide(UserRepository, provides=UserRepositoryProtocol)
    on_start = provide(StartInteractor)
    register_user = provide(RegisterUserGlobalyInteractor)
    unregister_user = provide(UnRegisterUserGlobalyInteractor)
    set_emoji = provide(SetEmojiGlobalyInteractor)
