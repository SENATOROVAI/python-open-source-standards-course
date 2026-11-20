"""Файл с ошибками типов: проверьте его линтерами."""

import os, sys


NAME: str = 10


def shout(text: str) -> str:
    return text + 1


def length(text: str) -> int:
    """Вернуть длину строки."""
    return text


HOME: str = os.getcwd(1)


def run() -> None:
    total: int = "10"
    print(shout(5))
    items: list[int] = []
    items.append("one")
    print(total.upper())


sys.exit(shout(None))
