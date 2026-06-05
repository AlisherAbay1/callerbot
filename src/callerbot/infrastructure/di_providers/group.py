from dishka import Provider, Scope, provide
from callerbot.application.interactors.group import (
    RegisterUserLocallyInteractor,
    JoinChatInteractor,
    CreateModelsInteractor,
)
from callerbot.application.services import (
    GetOrCreateChatMemberService,
    GetOrCreateUserService,
)


class GroupProvider(Provider):
    scope = Scope.REQUEST
    get_or_create_chat_member_service = provide(GetOrCreateChatMemberService)
    get_or_create_user_service = provide(GetOrCreateUserService)
    register_user_locally = provide(RegisterUserLocallyInteractor)
    join_chat = provide(JoinChatInteractor)
    create_models = provide(CreateModelsInteractor)
