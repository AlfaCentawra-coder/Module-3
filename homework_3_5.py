def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number = int(input("Введите число: "))
x = get_multiplied_digits(number)
print(x)