import re

input_string = 'MCMXCIV'
Roman_numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
subtraction_combos = ['IV','IX','XL','XC','CD','CM']


# if (1 <= len(input_string) < 15):
#     if (all(x in Roman_numerals for x in input_string)):
#         if (any(re.search(x, input_string) for x in subtraction_combos)):
#             print('subtraction')
#         else:
#             h = []    
#             for x in input_string:
#                 h.append(Roman_numerals[x])
#             answer = sum(h)
#             print(answer)
#     else:
#         print('Invalid entry')


print(str.find(input_string,'fr'))
