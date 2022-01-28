from singleton import Singleton, LazySingleton

if __name__ == '__main__':
    assert(id(Singleton()) == id(Singleton()))
    assert(id(LazySingleton.get_instance()) == id(LazySingleton.get_instance()))
