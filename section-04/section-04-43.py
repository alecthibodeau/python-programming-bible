# Section 4
# 43. Match Function

import re

pattern = re.compile('ell')
print(pattern.match("hello world"))
print(pattern.match("hello world", 1))

result = pattern.match('hello world')

# print(result.group(1))

# Output
# None
# <_sre.SRE_Match object at 0x7fb7c2f035e0>
