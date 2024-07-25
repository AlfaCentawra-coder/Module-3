def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params()
#print_params(b = 25)
#print_params(c = [1,2,3])
#print_params(1, 'привет', False, [1, 4, 648], "строка")

value_list = [False, 39.7, "Карта"]
value_dict = {'a': 17, 'b': True, 'c': "Привет"}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [54.32, 'Строка']

print_params(*value_list_2, 42)