data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  'Hello',
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

clear_data = []

a = sum(data_structure[0])
clear_data.append(a)
print(a)

for key, value in data_structure[1].items():
  clear_data.append(len(key) + value)
  print(len(key) + value)

for dict_element in data_structure[2]:
  if type(dict_element) == str or type(dict_element) == int:
    clear_data.append(dict_element)
    print(dict_element)
  elif type(dict_element) == dict:
    for key, value in dict_element.items():
      clear_data.append(len(key) + value)
      print(len(key) + value)

clear_data.append(len(data_structure[3]))
print(len(data_structure[3]))

for tuple_elements in data_structure[4]:
    for un_tuple_elements in tuple_elements:
      for un_un_tuple_elements in un_tuple_elements:
        for un_un_un_tuple_elements in un_un_tuple_elements:
          if type(un_un_un_tuple_elements) == str:
            clear_data.append(len(un_un_un_tuple_elements))
          elif type(un_un_un_tuple_elements) == int:
            clear_data.append(un_un_un_tuple_elements)
          elif type(un_un_un_tuple_elements) == tuple:
            for un_un_un_un_tuple_elements in un_un_un_tuple_elements:
              if type(un_un_un_un_tuple_elements) == str:
                clear_data.append(len(un_un_un_un_tuple_elements))
              elif type(un_un_un_un_tuple_elements) == int:
                clear_data.append(un_un_un_un_tuple_elements)

print(sum(clear_data))




#try:
#  a = x / y
#except ZeroDivisionError:
#  print ("?")
#else:
#  print ("a = ", a)
#finally:
#  print("finally")






