"""
TODO:

foo should return an integer argument.
"""


def foo():
    return 1


def should_pass():
    i: int = foo()


def should_fail():
    i: str = foo()
