from typing import (Any, Callable, Generic, Iterator, SupportsIndex, TypeVar,
                    Union)

_T = TypeVar("_T")
_V = TypeVar("_V")


class List(list, Generic[_T]):

    def __iter__(self) -> Iterator[_T]:
        return super().__iter__()

    def __getitem__(self, i: SupportsIndex) -> _T:
        return super().__getitem__(i)

    def find(self, fnc: Union[Callable[[_T], bool], _T], defaultValue=None) -> _T:
        if(callable(fnc)):
            return next((x for x in self if fnc(x)), defaultValue)
        if(fnc in self):
            return fnc
        return defaultValue

    def filter(self, fnc: Callable[[_T, int], bool]) -> "List[_T]":
        return List([x[1] for x in enumerate(self) if fnc(x[1], x[0])])

    def map(self, fnc: Callable[[_T], _V]) -> "List[_V]":
        return List([fnc(x) for x in self])

    def appendIfNew(self, elt: _T):
        if(elt in self):
            return False
        self.append(elt)
        return True

    def appendAllIfNew(self, *args: _T):
        result = True
        for elt in args:
            result = result and self.appendIfNew(elt)
        pass

    def appendIfNewAndDefined(self, elt: _T):
        if(elt in self or elt is None):
            return False
        self.append(elt)
        return True


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
