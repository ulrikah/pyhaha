import pytest


class Transaction:
    DEFAULT = "transactions"

    def echo(self):
        return self.DEFAULT

class FakeTransaction:
    DEFAULT = "fake"

def uppercase(self):
    return self.DEFAULT.upper()

def test_transaction():
    func = Transaction.echo
    transaction = Transaction()
    fake = FakeTransaction()
    assert func(transaction) == "transactions"
    assert func(fake) == "fake"
    Transaction.echo = uppercase
    assert func(transaction) == "transactions"
    assert func(fake) == "fake"
    func2 = Transaction.echo
    assert func2(transaction) == "TRANSACTIONS"
    print()

def test_method_deletion():
    class Delete:
        def f(self):
            return "hello"
        
    d = Delete()
    df = d.f
    del d
    assert df() == "hello"

