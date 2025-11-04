from iac_patterns.Fase2.Ejercicio21_singleton.singleton import ConfigSingleton
from iac_patterns.Fase2.Ejercicio22_factory.factory import NullResourceFactory
from iac_patterns.Fase2.Ejercicio23_prototype.prototype import ResourcePrototype

def test_singleton_meta():
    a = ConfigSingleton("X")
    b = ConfigSingleton("Y")
    assert a is b, "El patrón Singleton debe mantener una única instancia"

def test_prototype_clone_independent():
    proto = ResourcePrototype(NullResourceFactory.create("app"))
    c1 = proto.clone(lambda b: b.update({"extra": 1}))
    c2 = proto.clone(lambda b: b.update({"meta": 2}))
    assert "extra" not in c2.data and "meta" not in c1.data, "Los clones deben ser independientes"
