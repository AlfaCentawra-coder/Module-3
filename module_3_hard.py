data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    result = 0

    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            result += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            result += len(key) + calculate_structure_sum(value)
    elif isinstance(data, frozenset):
        for item in data:
            result += calculate_structure_sum(item)

    return result


result = calculate_structure_sum(data_structure)
print(result)






