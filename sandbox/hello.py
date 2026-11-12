def hello(name: str) -> str:
    return f"Bonjour {name}"


def hello_twice(name: str) -> str:
    """Return two greetings without duplicating formatting logic."""
    return f"{hello(name)} / {hello(name)}"
