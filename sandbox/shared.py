def shared() -> str:
    return "daemon"


def shared_twice() -> str:
    return shared() * 2
