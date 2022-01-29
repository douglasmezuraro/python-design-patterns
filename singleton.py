from typing import Any, Mapping, Iterable

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


class MetaClassSingletonExample(metaclass=MetaClassSingleton):
    pass
