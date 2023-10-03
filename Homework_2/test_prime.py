import prime


def test_is_prime():
    assert hasattr(
        prime, 'is_prime'), "Your prime.py script must have a method called is_prime"
    assert not prime.is_prime(1)
    assert prime.is_prime(2)
    assert not prime.is_prime(4)
    assert prime.is_prime(5)
    assert not prime.is_prime(12)
    assert prime.is_prime(179424673)
    assert not prime.is_prime(982451651)

