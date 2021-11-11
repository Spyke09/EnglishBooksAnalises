from pathlib import Path


def get_root(st: str) -> Path:
    return Path(__file__).parent.parent.joinpath(st)
