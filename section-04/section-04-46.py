# Section 4
# 46. Search & Replace

# Regular expression operations - https://docs.python.org/3/library/re.html

import re

string1 = 'quhw 9876 jhghjqw 89898; .aw wkaw'

# Eliminate all non-digit characters
result = re.sub(r'\D', '', string1)
print(result)

# Substitute all non-digit characters with a space
result = re.sub(r'\D', ' ', string1)
print(result)

# Substitute all non-digit characters with a dot
result = re.sub(r'\D', '.', string1)
print(result)

# Output
# 987689898
#      9876         89898
# .....9876.........89898..........
