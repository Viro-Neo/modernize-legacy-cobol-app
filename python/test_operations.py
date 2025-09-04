# test_operations.py

import pytest
import main
import operations


@pytest.fixture
def mock_balance(monkeypatch):
    balance = {'value': 1000.0}
    monkeypatch.setattr(operations, 'read_balance', lambda: balance['value'])
    monkeypatch.setattr(operations, 'write_balance', lambda v: balance.update({'value': v}))
    return balance


def test_TC01_view_balance(capsys, mock_balance):
    operations.view_balance()
    captured = capsys.readouterr()
    assert "Current balance: 1000.00" in captured.out


def test_TC02_credit_valid(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '200')
    operations.credit_account()
    assert mock_balance['value'] == 1200.0
    captured = capsys.readouterr()
    assert "Amount credited. New balance: 1200.00" in captured.out


def test_TC03_credit_zero(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '0')
    operations.credit_account()
    assert mock_balance['value'] == 1000.0
    captured = capsys.readouterr()
    assert "Amount credited. New balance: 1000.00" in captured.out


def test_TC04_credit_negative(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '-50')
    operations.credit_account()
    assert mock_balance['value'] == 1050.0
    captured = capsys.readouterr()
    assert "Amount credited. New balance: 1050.00" in captured.out


def test_TC05_debit_valid(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '500')
    operations.debit_account()
    assert mock_balance['value'] == 500.0
    captured = capsys.readouterr()
    assert "Amount debited. New balance: 500.00" in captured.out


def test_TC06_debit_insufficient(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '2000')
    operations.debit_account()
    assert mock_balance['value'] == 1000.0
    captured = capsys.readouterr()
    assert "Insufficient funds for this debit." in captured.out


def test_TC07_debit_zero(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '0')
    operations.debit_account()
    assert mock_balance['value'] == 1000.0
    captured = capsys.readouterr()
    assert "Amount debited. New balance: 1000.00" in captured.out


def test_TC08_debit_negative(monkeypatch, mock_balance, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '-100')
    operations.debit_account()
    assert mock_balance['value'] == 900.0
    captured = capsys.readouterr()
    assert "Amount debited. New balance: 900.00" in captured.out


def test_TC09_exit_program(monkeypatch, capsys):
    inputs = iter(['4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert "Exiting the program. Goodbye!" in captured.out
