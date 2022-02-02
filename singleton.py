from typing import Any, Mapping, Iterable
from sqlite3 import Cursor, connect

class Singleton(object):

    def __new__(cls) -> 'Singleton':
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


class LazySingleton(object):

    __instance = None

    @classmethod
    def get_instance(cls) -> 'LazySingleton':
        if not cls.__instance:
            cls.__instance = LazySingleton()

        return cls.__instance


class MonoStateSingleton(object):

    __state = {}

    def __new__(cls, *args: Iterable[Any], **kwargs: Mapping[str, Any]) -> 'MonoStateSingleton':
        obj = super(MonoStateSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state

        return obj


class MetaClassSingleton(type):

    __instances = {}

    def __call__(cls, *args: Iterable[Any], **kwargs: Mapping[str, Any]) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class DatabaseConnection(metaclass=MetaClassSingleton):

    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self) -> Cursor:
        if not self.__connection:
            self.__connection = connect('example.db')
            self.__cursor = self.__connection.cursor()

        return self.__cursor


if __name__ == '__main__':
    assert(id(Singleton()) == id(Singleton()))
    assert(id(LazySingleton.get_instance()) == id(LazySingleton.get_instance()))
    assert(id(DatabaseConnection()) == id(DatabaseConnection()))

    x, y = MonoStateSingleton(), MonoStateSingleton()
    x.foo = 'bar'
    assert(id(x) != id(y))
    assert(x.__dict__ == y.__dict__)
