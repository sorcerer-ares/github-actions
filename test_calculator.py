from calculator import add_numbers

def test_addition():
    # 2 + 2 should equal 4. But our broken function will return 0!
    assert add_numbers(2, 2) == 4
