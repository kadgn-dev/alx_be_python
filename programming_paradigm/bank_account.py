#!/usr/bin/env python3
"""
Module: bank_account
Defines a simple BankAccount class demonstrating OOP concepts.
"""

class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize the account with an optional starting balance.
        """
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount if funds are sufficient.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
