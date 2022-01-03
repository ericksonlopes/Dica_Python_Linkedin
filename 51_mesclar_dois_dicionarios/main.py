dict_0 = {"a": "1", "b": "2"}
dict_1 = {"c": "3", "d": "4"}

dict_2 = {**dict_0, **dict_1}

print(dict_2)
# OUT: {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
