from __future__ import annotations
from typing import Any, Iterable, Sequence, Union


class fastlist:
    def __init__(self, length: int = 0) -> None: ...
    @staticmethod
    def from_sequence(seq: Sequence[Any]) -> fastlist: ...
    @staticmethod
    def from_iterator(seq: Iterable[Any], sizehint: int = 0) -> fastlist: ...
    def __getitem__(self, index: Union[int, slice]) -> Any: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterable[Any]: ...
    def __repr__(self) -> str: ...
    def __setitem__(self, index: Union[int, slice], value: Any) -> None: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...
    def resize(self, newlength: int) -> None: ...
    def append(self, value: Any) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> fastlist: ...
    def insert(self, i: int, x: Any) -> None: ...
    def pop(self, i: int) -> Any: ...
    def remove(self, x: Any, starthint: int = 0) -> None: ...
    def reverse_range(self, start: int, end: int) -> None: ...
    def reverse(self) -> None: ...
