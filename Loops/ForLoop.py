# For Loops = execute a block of code a fixed nuber of times.

"""
for x in reversed(range(1,11)):
    print(x)

print("Happy New Year")
"""
# for counter in range(1,11):
#     print(counter)

# for x in range(1,11,2):
#     print(x)

"""
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
"""

unlucky_number = 13
for x in range(1,21):
    if x == unlucky_number:
        continue  # skip the iteration
        # break     # break the iteration completely and came out of the loop
    else:
        print(x)
