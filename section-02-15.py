# Section 2
# 15. Bitwise Operators

var1 = 13   # 1101
var2 = 5    # 0101

# 13    1101
# 5     0101
#       ----
# AND   0101 (5)
print(var1 & var2)

# 13    1101
# 5     0101
#       ----
# OR    1101 (13)
print(var1 | var2)

# 13    1101
# 5     0101
#       ----
# XOR   1000 (8)
print(var1 ^ var2)

# 13                1101
# Ones Complement   (-14) The bitwise inversion of x is defined as -(x+1)
print(~var1)

# 13                1101
# Binary Shift Left (11010 = 26)
print(var1 << 1)

# 13                1101
# Binary Shift Right (110 = 6)
print(var1 >> 1)
