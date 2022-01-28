from singleton import Singleton, LazySingleton, MonoStateSingleton

if __name__ == '__main__':
    assert(id(Singleton()) == id(Singleton()))
    assert(id(LazySingleton.get_instance()) == id(LazySingleton.get_instance()))

    x, y = MonoStateSingleton(), MonoStateSingleton()
    x.foo = 'bar'
    assert(id(x) != id(y))
    assert(x.__dict__ == y.__dict__)
