import pandas as pd
from typing import List, Dict, Union, Callable


from .functions import (
    character_deletion,
    character_duplication,
    line_segmentation,
    proximity_error,
    whitespace_segmentation,
    word_reversed,
    wordgrab_segementation,
)


def with_character_deletion(
    dataframe: pd.DataFrame, col: str, delete_idx: int
) -> pd.Series:
    return dataframe[col].apply(character_deletion, delete_idx=delete_idx)


def with_character_duplication(
    dataframe: pd.DataFrame, col: str, add_idx: int
) -> pd.Series:
    return dataframe[col].apply(character_duplication, add_idx=add_idx)


def with_line_segmentation(dataframe: pd.DataFrame, col: str) -> pd.Series:
    return dataframe[col].apply(line_segmentation)


def with_whitespace_segmentation(dataframe: pd.DataFrame, col: str) -> pd.Series:
    return dataframe[col].apply(whitespace_segmentation)


def with_word_reversed(
    dataframe: pd.DataFrame, col: str, reverse_idx: int
) -> pd.Series:
    return dataframe[col].apply(word_reversed, reverse_idx=reverse_idx)


def with_wordgrab_segementation(dataframe: pd.DataFrame, col: str) -> pd.Series:
    return dataframe[col].appy(wordgrab_segementation)


def with_proximity_error(
    dataframe: pd.DataFrame, col: str, error_rate: float
) -> pd.Series:
    return dataframe[col].apply(proximity_error, error_rate=error_rate)
