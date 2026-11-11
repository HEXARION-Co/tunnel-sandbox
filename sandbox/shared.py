def shared() -> str:
    return "lambda-daemon"


def shared_twice() -> str:
    return shared() * 2
