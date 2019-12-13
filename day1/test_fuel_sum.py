from fuel_sum import get_answer


def test_case0():
    assert get_answer([12]) == (2, 2)
    assert get_answer([14]) == (2, 2)
    assert get_answer([1969]) == (654, 966)
    assert get_answer([100756]) == (33583, 50346)
