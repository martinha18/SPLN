from ftk.base import ratio

def test_ratio():
    f1 = {"a": 49.3, "b": 50.7, "c": 100}
    f2 = {"a": 49.3, "b": 101.4}

    x = ratio(f1,f2)

    assert x["a"] == 1
    assert x["b"] == 0.5
    assert x["c"] == 0