from index_validator.validator import is_valid_index

def test_valid_indexes():
    assert is_valid_index("125009") == True
    assert is_valid_index("101000") == True

def test_invalid_indexes():
    assert is_valid_index("12345") == False
    assert is_valid_index("1234567") == False
    assert is_valid_index("125a09") == False
    assert is_valid_index("") == False