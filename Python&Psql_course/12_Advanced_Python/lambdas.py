l = lambda x: x > 5
print(l(10))

def alter(values, check):
  return [val for val in values if check(val)]


my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)

print(another_list)