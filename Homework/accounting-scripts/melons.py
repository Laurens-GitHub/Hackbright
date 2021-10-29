melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melon_flesh = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
}

melon_rind = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
}

melon_master = {}
for n in melon_names:
    melon_master[melon_names[n]] = melon_prices[n], melon_seedlessness[n], melon_flesh[n], melon_rind[n]
#print(melon_master)