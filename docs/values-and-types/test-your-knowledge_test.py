import pytest
    
def test_right_types():
    try:
        assert type(dictionary_of_things) == dict
        assert type(tuple_of_stuff) == tuple
        assert type(list_of_bits) == list
    except:
        print("something went wrong with your names and types, make sure your composite types have the right names labeled to the right types!")

def f():
    raise SystemExit(1)

def test_always_passes():
    assert True
    with pytest.raises(SystemExit):
        f()

def test_always_fails():
    assert False