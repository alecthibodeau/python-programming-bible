# Section 2
# 9. Tuples

awesomeList = ['Hello', 45, 'World', 4.5]

print(awesomeList)
print(awesomeList[0])
print(awesomeList[3])
print(awesomeList[0:2])

awesomeList[3] = 6

print(awesomeList[3])

awesomeTuple = ('Hello', 45, 'World', 4.5)

print(awesomeTuple)
print(awesomeTuple[0])
print(awesomeTuple[3])
print(awesomeTuple[0:2])

awesomeTuple[3] = 6

print(awesomeTuple[3])

# The above code example throws an error:
# Traceback (most recent call last):
#   File "section-02-09.py", line 22, in <module>
#     awesomeTuple[3] = 6
# TypeError: 'tuple' object does not support item assignment
