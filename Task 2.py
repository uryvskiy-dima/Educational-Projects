"""
Кодирование длин серий — это базовый алгоритм сжатия данных.
В этой задаче мы реализуем одну из самых простых его вариантов.

На вход алгоритму подаётся строка, содержащая символы латинского алфавита. Эта строка разбивается на группы одинаковых
символов, идущих подряд ("серии"). Каждая серия характеризуется повторяющимся символом и количеством повторений.
Именно эта информация и записывается в код: сначала пишется длина серии повторяющихся символов, затем сам символ.
У серий длиной в один символ количество повторений будем опускать.

Например, рассмотрим строку
aaabccccCCaB
Разобъём её на серии
aaa b cccc CC a B
После чего закодируем серии и получим итоговую строку, которую и будем считать результатом работы алгоритма.
3ab4c2CaB
Формат ввода:
Одна строка, содержащая произвольные символы латинского алфавита.

Формат вывода:
Строка, содержащая закодированную последовательность.

Sample Input 1:
aaabccccCCaB
Sample Output 1:

3ab4c2CaB
Sample Input 2:
a
Sample Output 2:
a
"""

input_string = input()
i = 0
count = 1
while i < len(input_string):
    if i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
        count += 1
    else:
        if count == 1:
            print(input_string[i], end='')
        else:
            print(str(count) + input_string[i], end='')
        count = 1
    i += 1