import random

print(random.choices([1, 2, 3, 4, 5, 6], k=2))
# [2, 1]

print(random.choices([1, 2, 3, 4, 5, 6], k=3))
# [4, 6, 2]

# Com pesos
print(random.choices([1, 2, 3, 4, 5, 6], k=4, weights=[1, 5, 1, 1, 1, 1]))
# [2, 3, 4, 2]
