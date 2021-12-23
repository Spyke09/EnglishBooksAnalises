from pathlib import Path


def get_root(st: str):
    return Path(__file__).parent.parent.joinpath(st)
