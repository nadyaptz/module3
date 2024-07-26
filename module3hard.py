
def calculate_structure_sum(data_structure, summa):
    if isinstance(data_structure, dict):
        summa=int(calculate_structure_sum(list(data_structure.keys()), summa))
        summa=int(calculate_structure_sum(list(data_structure.values()), summa))
        return summa
    if isinstance(data_structure, list) or isinstance(data_structure, set) or isinstance(data_structure, tuple):
        for element in data_structure:
            summa = calculate_structure_sum(element, summa)
        return summa
    if isinstance(data_structure, str):
        summa += len(data_structure)
        return summa
    if isinstance(data_structure, int) or isinstance(data_structure, float):
        summa += data_structure
        return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
summa=0
print(calculate_structure_sum(data_structure, summa))


