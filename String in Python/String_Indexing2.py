# indexing -> [start : end : steps]  (start=inclusive, end=exclusive)

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1:])
print(credit_number[::2])

last_digits=credit_number[-4:]
print(f"XXXX-XXXX-XXXX{last_digits}")

credit_number = credit_number[::-1]  # reverses the total string characters
print(credit_number)