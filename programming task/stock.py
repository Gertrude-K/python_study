prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]


def calculate_total_value(products):
    total= 0
    for product in products:
        total += int(product[-1])
    return total


print(f"The total stock is: {calculate_total_value(prods)}")