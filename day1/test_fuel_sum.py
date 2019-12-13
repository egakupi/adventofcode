from fuel_sum import fuel_sum


def test_case0():
    assert fuel_sum([12]) == 2
    assert fuel_sum([14]) == 2
    assert fuel_sum([1969]) == 654
    assert fuel_sum([100756]) == 33583