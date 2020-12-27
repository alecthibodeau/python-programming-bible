# Section 2
# 22. Loop Control Statements

var1 = "Hello World"

for character in var1:
    if character == ' ':
      print("There was a space, oh no")
      break
    print(character)

for character in var1:
    if character == ' ':
      print("There was a space, let's skip this iteration")
      continue
    print(character)

for character in var1:
    if character == ' ':
      pass # some sort of note
      print("Passing this over")
    print(character)

# Output
# H
# e
# l
# l
# o
# There was a space, oh no
# H
# e
# l
# l
# o
# There was a space, let's skip this iteration
# W
# o
# r
# l
# d
# H
# e
# l
# l
# o
# Passing this over

# W
# o
# r
# l
# d
