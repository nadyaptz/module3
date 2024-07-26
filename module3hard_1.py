global summa
summa = 0


def calculate_structure_sum(data_structure):
    global summa
    if isinstance(data_structure, dict):
        calculate_structure_sum(list(data_structure.keys()))
        calculate_structure_sum(list(data_structure.values()))
    if isinstance(data_structure, list) or isinstance(data_structure, set) or isinstance(data_structure, tuple):
        for element in data_structure:
            calculate_structure_sum(element)
    if isinstance(data_structure, str):
        summa += len(data_structure)
        return
    if isinstance(data_structure, int) or isinstance(data_structure, float):
        summa += data_structure
        return

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

calculate_structure_sum(data_structure)
print(summa)
