import pandas as pd

from loudred.dataframe_helpers import (
    with_character_deletion,
    with_line_segmentation,
    with_character_duplication,
    with_whitespace_segmentation,
    with_proximity_error,
    with_word_reversed,
    with_wordgrab_segementation
)
# def test_character_deletion_assigned() -> None:
#     test_str: str = "string"
#     validation_on_idx: str = "sting"
#     result = with_character_deletion(test_str, delete_idx=2)
#     assert validation_on_idx == result

# def test_character_deletion_unassigned() -> None:
#     test_str: str = "string"
#     result = with_character_deletion(test_str)

# test_character_deletion_assigned()
# test_character_deletion_unassigned()

df = pd.DataFrame({"text": ["string is here"]})

# print(df.text.apply(with_character_deletion,delete_idx=1))
print(df.pipe(with_character_deletion, col="text", delete_idx=None))