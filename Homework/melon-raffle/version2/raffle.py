"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
import random
from random import choice
from customers import get_customers_from_file

def pick_winner(get_customers_from_file):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(get_customers_from_file)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)