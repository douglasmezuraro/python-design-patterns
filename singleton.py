class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


class LazySingleton(object):

    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()

        return cls.__instance
