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
        melon_dic[MelonType.code] = [MelonType.name, MelonType.code, MelonType.first_harvest, MelonType.color, MelonType.is_seedless, MelonType.is_bestseller]

    return melon_dic
    # name, code, first_harvest, color, is_seedless, is_bestseller
    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
       # Needs __init__ and is_sellable methods
    def __init__(
        self, name, code, shape_rating, color_rating, harvested_from, harvested_by
    ):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != "Field 3":
            self.sellability = True
        else:
            self.sellability = False


def make_melons(melon_type):
    """Returns a list of Melon objects."""

    melon_list = []

    Melon_1 = Melon('Melon_1', 'yw', 8, 7, 'Field 2', 'Sheila')
    melon_list.append(Melon_1)

    # melon_list(Melon_1) = current_value.extend(dict_from_prev[code for melon 1])

    Melon_2 = Melon('Melon_2', 'yw', 3, 4, 'Field 2', 'Sheila')
    melon_list.append(Melon_2)

    Melon_3 = Melon('Melon_3', 'yw', 9, 8, 'Field 3', 'Sheila')
    melon_list.append(Melon_3)

    Melon_4 = Melon('Melon_4', 'cas', 10, 6, 'Field 35', 'Sheila')
    melon_list.append(Melon_4)

    Melon_5 = Melon('Melon_5', 'cren', 8, 9, 'Field 35', 'Michael')
    melon_list.append(Melon_5)

    Melon_6 = Melon('Melon_6', 'cren', 8, 2, 'Field 35', 'Michael')
    melon_list.append(Melon_6)

    Melon_7 = Melon('Melon_7', 'cren', 2, 3, 'Field 4', 'Michael')
    melon_list.append(Melon_7)

    Melon_8 = Melon('Melon_8', 'musk', 6, 7, 'Field 4', 'Michael')
    melon_list.append(Melon_8)

    Melon_9 = Melon('Melon_9', 'yw', 7, 10, 'Field 3', 'Sheila')
    melon_list.append(Melon_9)


    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        melon.is_sellable()
        if melon.sellability == True:
            sellable_text = 'CAN BE SOLD'
        else:
            sellable_text = 'NOT SELLABLE'

        print(f'{melon.name}: Harvested by {melon.harvested_by} from {melon.harvested_from} ({sellable_text})')


