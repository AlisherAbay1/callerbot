from dishka import Provider, Scope, provide
from callerbot.application.interactors.private import (
    StartInteractor,
    RegisterUserGlobalyInteractor,
    UnRegisterUserGlobalyInteractor,
    SetEmojiGlobalyInteractor,
    UnSetEmojiGlobalyInteractor,
    GetSettingsInteractor,
)


class PrivateProvider(Provider):
    scope = Scope.REQUEST
    on_start = provide(StartInteractor)
    register_user = provide(RegisterUserGlobalyInteractor)
    unregister_user = provide(UnRegisterUserGlobalyInteractor)
    set_emoji = provide(SetEmojiGlobalyInteractor)
    unset_emoji = provide(UnSetEmojiGlobalyInteractor)
    get_settings = provide(GetSettingsInteractor)
