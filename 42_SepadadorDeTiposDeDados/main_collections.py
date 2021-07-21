from collections import defaultdict

lista = [[1, 2, 3], 'Python', 1, 1.2, [4, 5], 2, 'C++', 3.5]
dicio = defaultdict(list)
[dicio[type(item)].append(item) for item in lista]

print(dicio)
