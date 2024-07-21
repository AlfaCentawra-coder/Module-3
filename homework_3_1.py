def string_info(stroka):
    global calls
    list_ = [len(stroka), stroka.upper(), stroka.lower()]
    x = tuple(list_)
    count_calls()
    return print(x)

def is_contains(stroka, listok):
    global calls
    upper_stroka = stroka.upper()
    for i in range(len(listok)):
        listok[i] = listok[i].upper()
    count_calls()
    return print(upper_stroka in listok)

def count_calls():
    global calls
    calls += 1

calls = 0
stroka = input("Введите слово: ")
listok = [str(x) for x in input("Введите несколько слов без запятых: ").split()]
string_info(stroka)
is_contains(stroka, listok)
print(calls)
