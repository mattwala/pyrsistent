# flake8: noqa: E704
# from https://gist.github.com/WuTheFWasThat/091a17d4b5cab597dfd5d4c2d96faf09
# Stubs for pyrsistent (Python 3.6)
#
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Hashable
from typing import Iterator
from typing import Iterable
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import AbstractSet
from typing import Sized
from typing import Set
from typing import Tuple
from typing import TypeVar
from typing import Type
from typing import Union
from typing import overload

T = TypeVar('T')
KT = TypeVar('KT')
VT = TypeVar('VT')


class PMap(Mapping[KT, VT], Hashable):
    def __add__(self, other: PMap[KT, VT]) -> PMap[KT, VT]: ...
    def __getitem__(self, key: KT) -> VT: ...
    def __getattr__(self, key: str) -> VT: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[KT]: ...
    def __len__(self) -> int: ...
    def copy(self) -> PMap[KT, VT]: ...
    def discard(self, key: KT) -> PMap[KT, VT]: ...
    def evolver(self) -> PMapEvolver[KT, VT]: ...
    def iteritems(self) -> Iterable[Tuple[KT, VT]]: ...
    def iterkeys(self) -> Iterable[KT]: ...
    def itervalues(self) -> Iterable[VT]: ...
    def remove(self, key: KT) -> PMap[KT, VT]: ...
    def set(self, key: KT, val: VT) -> PMap[KT, VT]: ...
    def transform(self, *transformations: Any) -> PMap[KT, VT]: ...
    def update(self, *args: Mapping) -> PMap[KT, VT]: ...
    def update_with(self, update_fn: Callable[[VT, VT], VT], *args: Mapping) -> Any: ...


class PMapEvolver(Generic[KT, VT]):
    def __delitem__(self, key: KT) -> None: ...
    def __getitem__(self, key: KT) -> VT: ...
    def __len__(self) -> int: ...
    def __setitem__(self, key: KT, val: VT) -> None: ...
    def is_dirty(self) -> bool: ...
    def persistent(self) -> PMap[KT, VT]: ...
    def remove(self, key: KT) -> PMapEvolver[KT, VT]: ...
    def set(self, key: KT, val: VT) -> PMapEvolver[KT, VT]: ...


class PVector(Sequence[T], Hashable):
    def __add__(self, other: PVector[T]) -> PVector[T]: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> PVector[T]: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __mul__(self, other: PVector[T]) -> PVector[T]: ...
    def append(self, val: T) -> PVector[T]: ...
    def delete(self, index: int, stop: Optional[int]) -> PVector[T]: ...
    def evolver(self) -> PVectorEvolver[T]: ...
    def extend(self, obj: Iterable[T]) -> PVector[T]: ...
    def tolist(self) -> List[T]: ...
    def mset(self, *args: Iterable[Union[T, int]]) -> PVector[T]: ...
    def remove(self, value: T) -> PVector[T]: ...
    # Not compatible with MutableSequence
    def set(self, i: int, val: T) -> PVector[T]: ...
    def transform(self, *transformations: Any) -> PVector[T]: ...


class PVectorEvolver(Sequence[T], Sized):
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    # Not actually supported
    @overload
    def __getitem__(self, index: slice) -> PVectorEvolver[T]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, index: int, val: T) -> None: ...
    def append(self, val: T) -> PVectorEvolver[T]: ...
    def delete(self, value: T) -> PVectorEvolver[T]: ...
    def extend(self, obj: Iterable[T]) -> PVectorEvolver[T]: ...
    def is_dirty(self) -> bool: ...
    def persistent(self) -> PVector[T]: ...
    def set(self, i: int, val: T) -> PVectorEvolver[T]: ...


class PSet(AbstractSet[T], Hashable):
    def __contains__(self, element: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
    def add(self, element: T) -> PSet[T]: ...
    def copy(self) -> PSet[T]: ...
    def difference(self, iterable: Iterable) -> PSet[T]: ...
    def discard(self, element: T) -> PSet[T]: ...
    def evolver(self) -> PSetEvolver[T]: ...
    def intersection(self, iterable: Iterable) -> PSet[T]: ...
    def issubset(self, iterable: Iterable) -> bool: ...
    def issuperset(self, iterable: Iterable) -> bool: ...
    def remove(self, element: T) -> PSet[T]: ...
    def symmetric_difference(self, iterable: Iterable[T]) -> PSet[T]: ...
    def union(self, iterable: Iterable[T]) -> PSet[T]: ...
    def update(self, iterable: Iterable[T]) -> PSet[T]: ...


class PSetEvolver(Generic[T], Sized):
    def __len__(self) -> int: ...
    def add(self, element: T) -> PSetEvolver[T]: ...
    def is_dirty(self) -> bool: ...
    def persistent(self) -> PSet[T]: ...
    def remove(self, element: T) -> PSetEvolver[T]: ...


class PBag(Generic[T], Sized, Hashable):
    def __add__(self, other: PBag[T]) -> PBag[T]: ...
    def __and__(self, other: PBag[T]) -> PBag[T]: ...
    def __contains__(self, elem: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
    def __or__(self, other: PBag[T]) -> PBag[T]: ...
    def __sub__(self, other: PBag[T]) -> PBag[T]: ...
    def add(self, elem: T) -> PBag[T]: ...
    def count(self, elem: T) -> int: ...
    def remove(self, elem: T) -> PBag[T]: ...
    def update(self, iterable: Iterable[T]) -> PBag[T]: ...


class PDeque(Sequence[T], Hashable):
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> PDeque[T]: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: PDeque[T]) -> bool: ...
    def append(self, elem: T) -> PDeque[T]: ...
    def appendleft(self, elem: T) -> PDeque[T]: ...
    def extend(self, iterable: Iterable[T]) -> PDeque[T]: ...
    def extendleft(self, iterable: Iterable[T]) -> PDeque[T]: ...
    @property
    def left(self) -> T: ...
    # The real return type is Integral according to what pyrsistent
    # checks at runtime but mypy doesn't deal in numeric.*:
    # https://github.com/python/mypy/issues/2636
    @property
    def maxlen(self) -> int: ...
    def pop(self, count: int = 1) -> PDeque[T]: ...
    def popleft(self, count: int = 1) -> PDeque[T]: ...
    def remove(self, elem: T) -> PDeque[T]: ...
    def reverse(self) -> PDeque[T]: ...
    @property
    def right(self) -> T: ...
    def rotate(self, steps: int) -> PDeque[T]: ...


class PList(Sequence[T], Hashable):
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> PList[T]: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: PList[T]) -> bool: ...
    def __gt__(self, other: PList[T]) -> bool: ...
    def cons(self, elem: T) -> PList[T]: ...
    @property
    def first(self) -> T: ...
    def mcons(self, iterable: Iterable[T]) -> PList[T]: ...
    def remove(self, elem: T) -> PList[T]: ...
    @property
    def rest(self) -> PList[T]: ...
    def reverse(self) -> PList[T]: ...
    def split(self, index: int) -> Tuple[PList[T], PList[T]]: ...

T_PClass = TypeVar('T_PClass', bound='PClass')

class PClass(Hashable):
    def __new__(cls, **kwargs: Any): ...
    def set(self: T_PClass, *args: Any, **kwargs: Any) -> T_PClass: ...
    @classmethod
    def create(
        cls: Type[T_PClass],
        kwargs: Any,
        _factory_fields: Optional[Any] = ...,
        ignore_extra: bool = ...,
    ) -> T_PClass: ...
    def serialize(self, format: Optional[Any] = ...): ...
    def transform(self, *transformations: Any): ...
    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def __hash__(self): ...
    def __reduce__(self): ...
    def evolver(self) -> PClassEvolver: ...
    def remove(self: T_PClass, name: Any) -> T_PClass: ...

class PClassEvolver:
    def __init__(self, original: Any, initial_dict: Any) -> None: ...
    def __getitem__(self, item: Any): ...
    def set(self, key: Any, value: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def remove(self, item: Any): ...
    def __delitem__(self, item: Any) -> None: ...
    def persistent(self) -> PClass: ...
    def __getattr__(self, item: Any): ...



class CheckedPMap(PMap[KT, VT]):
    __key_type__: Type[KT]
    __value_type__: Type[VT]
    def __new__(cls, source: Mapping[KT, VT] = ..., size: int = ...) -> CheckedPMap: ...
    @classmethod
    def create(cls, source_data: Mapping[KT, VT], _factory_fields: Any = ...) -> CheckedPMap[KT, VT]: ...
    def serialize(self, format: Optional[Any] = ...) -> Dict[KT, VT]: ...


class CheckedPVector(PVector[T]):
    __type__: Type[T]
    def __new__(self, initial: Iterable[T] = ...) -> CheckedPVector: ...
    @classmethod
    def create(cls, source_data: Iterable[T], _factory_fields: Any = ...) -> CheckedPVector[T]: ...
    def serialize(self, format: Optional[Any] = ...) -> List[T]: ...


class CheckedPSet(PSet[T]):
    __type__: Type[T]
    def __new__(cls, initial: Iterable[T] = ...) -> CheckedPSet: ...
    @classmethod
    def create(cls, source_data: Iterable[T], _factory_fields: Any = ...) -> CheckedPSet[T]: ...
    def serialize(self, format: Optional[Any] = ...) -> Set[T]: ...


class InvariantException(Exception):
    invariant_errors: Tuple[Any, ...] = ...  # possibly nested tuple
    missing_fields: Tuple[str, ...] = ...
    def __init__(
        self,
        error_codes: Any = ...,
        missing_fields: Any = ...,
        *args: Any,
        **kwargs: Any
    ) -> None: ...


class CheckedTypeError(TypeError):
    source_class: Type[Any]
    expected_types: Tuple[Any, ...]
    actual_type: Type[Any]
    actual_value: Any
    def __init__(
        self,
        source_class: Any,
        expected_types: Any,
        actual_type: Any,
        actual_value: Any,
        *args: Any,
        **kwargs: Any
    ) -> None: ...


class CheckedKeyTypeError(CheckedTypeError): ...
class CheckedValueTypeError(CheckedTypeError): ...
class CheckedType: ...


class PTypeError(TypeError):
    source_class: Type[Any] = ...
    field: str = ...
    expected_types: Tuple[Any, ...] = ...
    actual_type: Type[Any] = ...
    def __init__(
        self,
        source_class: Any,
        field: Any,
        expected_types: Any,
        actual_type: Any,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
