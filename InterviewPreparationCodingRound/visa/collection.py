from collections import deque, namedtuple, defaultdict, Counter, OrderedDict, ChainMap

# List Example
my_list = [10, 20, 30, 40]
print("List:")
for element in my_list:
    print(element)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Tuple Example
my_tuple = (1, 2, 3, 4)
print("\nTuple:")
for element in my_tuple:
    print(element)

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

# Set Example
my_set = {100, 200, 300, 400}
print("\nSet:")
for element in my_set:
    print(element)

# Sets are unordered, no while loop example for index-based access

# Dictionary Example
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

keys = list(my_dict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key}: {my_dict[key]}")
    i += 1

# String Example
my_string = "hello"
print("\nString:")
for char in my_string:
    print(char)

i = 0
while i < len(my_string):
    print(my_string[i])
    i += 1

# Deque Example
my_deque = deque(['apple', 'banana', 'cherry'])
print("\nDeque:")
for element in my_deque:
    print(element)

i = 0
while i < len(my_deque):
    print(my_deque[i])
    i += 1

# Namedtuple Example
Point = namedtuple('Point', ['x', 'y'])
p = Point(4, 5)
print("\nNamedtuple:")
for value in p:
    print(value)

i = 0
while i < len(p):
    print(p[i])
    i += 1

# Defaultdict Example
my_defaultdict = defaultdict(int)
my_defaultdict['apple'] += 1
my_defaultdict['banana'] += 2
print("\nDefaultdict:")
for key in my_defaultdict:
    print(f"{key}: {my_defaultdict[key]}")

keys = list(my_defaultdict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key}: {my_defaultdict[key]}")
    i += 1

# Counter Example
my_counter = Counter(['apple', 'banana', 'apple', 'cherry'])
print("\nCounter:")
for key, count in my_counter.items():
    print(f"{key}: {count}")

keys = list(my_counter.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key}: {my_counter[key]}")
    i += 1

# OrderedDict Example
my_ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
print("\nOrderedDict:")
for key, value in my_ordered_dict.items():
    print(f"{key}: {value}")

keys = list(my_ordered_dict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key}: {my_ordered_dict[key]}")
    i += 1

# ChainMap Example
dict1 = {'a': 1}
dict2 = {'b': 2}
my_chainmap = ChainMap(dict1, dict2)
print("\nChainMap:")
for key, value in my_chainmap.items():
    print(f"{key}: {value}")

keys = list(my_chainmap.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key}: {my_chainmap[key]}")
    i += 1
