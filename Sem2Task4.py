"""Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

number = int(input("Введите количество элементов списка: "))
one_list = []
i = 0
j = 0
while i < number:
    one_list.append(input("Введите значение списка: "))
    i += 1
i = 0
print(one_list)
for i in range(int(len(one_list)/2)):
        one_list[j], one_list[j + 1] = one_list[j + 1], one_list[j]
        j += 2
print(one_list)