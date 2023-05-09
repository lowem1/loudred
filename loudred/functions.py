import numpy as np
from typing import List, Dict, Callable, Union
from .util import proximity_map


def whitespace_segmentation(s: str) -> str:
    str_builder: List[str] = []
    for char in s:
        str_builder.extend([char, " "])
    return "".join(str_builder)


def character_deletion(s: str, delete_idx: int = None) -> str:
    str_builder: List[str] = []
    delete_idx = delete_idx if delete_idx else np.random.randint(len(s))
    for i, char in enumerate(s):
        if i != delete_idx:
            str_builder.append(char)
    return "".join(str_builder)


def character_duplication(s: str, add_idx: int = None) -> str:
    str_builder: List[str] = []
    add_idx = add_idx if add_idx else np.random.randint(len(s))
    for i, char in enumerate(s):
        if i == add_idx:
            str_builder.append(char)
        str_builder.append(char)
    return "".join(str_builder)


def line_segmentation(s: str) -> str:
    return "\n".join(s.split(" "))


def word_reversed(s: str, reverse_idx: int = None) -> str:
    str_builder: List[str] = []
    tmp = s.split(" ")
    reverse_idx = reverse_idx if reverse_idx else np.random.randint(len(tmp))
    for i, _ in enumerate(tmp):
        if i == reverse_idx:
            str_builder.append(_[::-1])
        else:
            str_builder.append(_)
    return " ".join(str_builder)


def wordgrab_segementation(s: str) -> str:
    str_builder: List[str] = s.split(" ")
    np.random.shuffle(str_builder)
    return " ".join(str_builder)


def proximity_error(s: str, error_rate: float = 0.1) -> str:
    def generate_error(s: str) -> str:
        proximity_errs = proximity_map[s]
        rand_idx = np.random.randint(len(proximity_errs))
        return proximity_errs[rand_idx]

    error_rate = error_rate if error_rate else 0
    str_builder: List[str] = []
    str_builder = list(s)
    proba: int = round(len(s) * error_rate)
    for i in range(proba):
        rand_idx = np.random.randint(len(s))
        for j, _ in enumerate(str_builder):
            if j == rand_idx and _ in proximity_map.keys():
                str_builder[j] = generate_error(_)
            elif j == rand_idx and _ not in proximity_map.keys():
                str_builder[j] = generate_error("[OVERRIDE]")
    return "".join(str_builder)
