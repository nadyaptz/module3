values_list = [True, 'Nadya', 1977]
values_dict = {'a': False, 'b': 'Fomina', 'c': 28}
values_list_2 = ['Sasha', 17]
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, c=False)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)