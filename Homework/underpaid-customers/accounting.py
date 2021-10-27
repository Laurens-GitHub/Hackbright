melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

# Lauren's function:

def accounting():
    data_file = open("customer-orders.txt")

    for line in data_file:
        line = line.rstrip()
        data = line.split('|')
        account_number = data[0]
        customer_name = data[1]
        melons_purchased = float(data[2])
        amount_paid = float(data[3])
        # overpaid = 0
        # underpaid = 0
        # settled = 0
        if amount_paid < (melons_purchased*melon_cost):
            print(f"{customer_name} has underpaid by ${(melons_purchased*melon_cost)-(amount_paid)}")
            #underpaid = underpaid + 1
        elif amount_paid > (melons_purchased*melon_cost):
            print(f"{customer_name} has overpaid by ${(amount_paid)-(melons_purchased*melon_cost)}")
            # overpaid = overpaid + 1
        else:
            print(f"{customer_name}'s account is settled.")  
            # settled = settled + 1
    data_file.close()
# extra idea: print the total number of underpaid, overpaid and settled accounts at the
# end of the loop

accounting()