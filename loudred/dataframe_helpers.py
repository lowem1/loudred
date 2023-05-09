import pandas as pd
from typing import List, Dict, Union, Callable, Optional


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
    series: pd.Series, delete_idx: Optional[int] = None
) -> pd.Series:
    return series.apply(character_deletion, delete_idx=delete_idx)


def with_character_duplication(
    series: pd.Series, add_idx: Optional[int] = None
) -> pd.Series:
    return series.apply(character_duplication, add_idx=add_idx)


def with_line_segmentation(series: pd.Series) -> pd.Series:
    return series.apply(line_segmentation)


def with_whitespace_segmentation(series: pd.Series) -> pd.Series:
    return series.apply(whitespace_segmentation)


def with_word_reversed(
    series: pd.Series, reverse_idx: Optional[int] = None
) -> pd.Series:
    return series.apply(word_reversed, reverse_idx=reverse_idx)


def with_wordgrab_segementation(series: pd.Series) -> pd.Series:
    return series.apply(wordgrab_segementation)


def with_proximity_error(
    series: pd.Series, error_rate: Optional[float] = None
) -> pd.Series:
    return series.apply(proximity_error, error_rate=error_rate)
