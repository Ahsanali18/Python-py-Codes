#complement of 1 -> 0
#complement of 0 -> 1
print(f"Complement of 12 is: {~12}")  #complement of 12 = (00001100) -> ~(11110011)

# Bitwise & operator
print(f"16 & 18 is: {16 & 18}") 
# Solution
# 16      : 10000
# 18      : 10010
# 16 & 18 : 10000 = 16

# Bitwise | operator
print(f"16 | 18 is: {16 | 18}")
# Solution
# 16      : 10000
# 18      : 10010
# 16 | 18 : 10010 = 18

# XOR Operator
# 0 0 -> 0
# 1 0 -> 1
# 0 1 -> 1
# 1 1 -> 0
print(f"16 ^ 18 is: {16^18}")
# Solution
# 16      : 10000
# 18      : 10010
# 16 ^ 18 : 00010 = 2

# Left shift << operator
print(f"4 << 2 is: {4<<2}")

# Right Shift >> operator
print(f"4 >> 2 is: {4>>2}")