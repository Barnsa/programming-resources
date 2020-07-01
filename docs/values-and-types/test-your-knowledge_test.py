import importlib

# moduleName = "docs.values-and-types.test-your-knowledge"
moduleName = "test-your-knowledge"
tyk = importlib.import_module(moduleName)

def type_error():
    raise TypeError("One of the variables were the wrong type, check composite types and try again.")

def name_error():
    raise NameError("One of your composite types was named wrong, check the spelling and try again.")

#@pytest.mark.fail(raises=TypeError)    
def test_right_types():
    """Check that all of the variables are correctly named and are of the right type"""
    assert type(tyk.dictionary_of_things) == dict, "dictionary_of_things should be a dictionary type object"
    assert type(tyk.tuple_of_stuff) == tuple, "tuple_of_stuff should be a tuple type object"
    assert type(tyk.list_of_bits) == list, "list_of_bits should be a list type object"
# except:
#         print("something went wrong with your names and types, make sure your composite types have the right names labeled to the right types!")

def test_right_names():
    """ check all the names are right for each of the composite types"""
    pass
    
def test_dictionary_values():
    """ test the dictionary meets params """
    assert tyk.dictionary_of_things is not None
    
def test_list_values():
    """make sure list meets requirements """ 
    pass

def test_tuple_values():
    """ make sure tuples meet requirements """
    pass 


### Test code to make sure that your code works and passes inspection
if __name__ == "__main__":
    import os
    path = os.getcwd()
    os.system("pytest " + os.getcwd())
