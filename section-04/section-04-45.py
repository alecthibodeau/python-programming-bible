# Section 4
# 45. Advanced Expressions

# Regular expression operations - https://docs.python.org/3/library/re.html

import re

string1 = 'Hello world is awesome'

# Three search parameters...
# 1) The pattern you want to match to
# 2) The string you're checking inside
# 3) The flags (separated by a pipe): "re.M" means multi-line, "re.I" means case-insensitive
result = re.search(r'(.*) world (.*?) .*', string1, re.M | re.I)

if (result):
    print(result.group())
    print(result.group(1))
    print(result.group(2))
else:
    print('No result')

# Output
# Hello world is awesome
# Hello
# is
