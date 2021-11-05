############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""


        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless =is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("Muskmelon","musk",1998,"green",True,True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("Casaba", "cas", 2003, "orange", False, False)
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")
    all_melon_types.append(cas)

    cren = MelonType("Crenshaw", "cren", 1996, "green", True, False)
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("Yellow Watermelon", "yw", 2013,"yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for MelonType in melon_types:
        print(f"{MelonType.name} pairs well with:")
        for pairing in MelonType.pairings:
            print (f"- {pairing}")
        print()
# Casaba pairs with
# - mint
# - strawberries


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dic = {}

    for MelonType in melon_types:
        melon_dic[MelonType.code] = MelonType.name, MelonType.code, MelonType.first_harvest, MelonType.color, MelonType.is_seedless, MelonType.is_bestseller

    return melon_dic
    # name, code, first_harvest, color, is_seedless, is_bestseller
    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest