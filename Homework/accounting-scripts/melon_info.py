"""Print out all the melons in our inventory."""


from melons import melon_master


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_master.keys():
    print_melon(i, melon_master[i][1], melon_master[i][0])
