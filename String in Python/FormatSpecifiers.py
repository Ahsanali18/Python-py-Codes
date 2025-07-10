# format specifiers = {value:flags} format a value based on what flags are inserted.

price1 = 3.14159
price2 = -9879.65
price3 = 12.34

# print(f"Price 1 is ${price1:.3f}")
# print(f"Price 2 is ${price2:.3f}")
# print(f"Price 3 is ${price3:.3f}")

# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# Left Justified
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# Right Justified
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

# Centered Alligned
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# Postive and Negative numbers preceedition
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")