# Блок 1

# EASY

# Написать простую функцию, которая на вход принимает два числа и 
# возвращает результат их сложения.
def foo(a:int, b:int):
    return a+b

# Записать эту функцию в произвольную переменную. 
# Напечатать эту переменную на экран. Что вы видите?

f = foo
# print(f)  # <function foo at 0x7f95120d1f70>

# Вызвать функцию суммирования через переменную,
# в которую вы только что её записали.

# print(f(2, 4))  # 6

# MEDIUM
# Написать функцию, которая на вход будет принимать 
# произвольное количество аргументов и возвращать их сумму.
def summator(*args:int):
    return sum(args)

# print(summator(2,4,6,8))  # 20

# В сигнатуре функции объявить 4 обязательных аргумента, 
# но оставить возможность передавать в неё сколько угодно дополнительных аргументов
def summator(a:int,b:int,c:int,d:int,*args:int):
    return a+b+c+d+sum(args)

# print(summator(1,2,3,4,5,6,7))  # 28

# print(summator(1))  # summator() missing 3 required positional arguments: 'b', 'c', and 'd'
# аргументы b,c,d - обязательные позиционные аргументы, которые необходимо передавать при вызове функции

# print(summator(1,2,3,4, a=1))  # summator() got multiple values for argument 'a'
# аргумента а был передан дважды, что вызвало ошибку TypeError

numbers = (1,2,3,4)
# print(summator(*numbers))  # 10 (элементы кортежа записались в позиционные аргументы)
# print(summator(1,2,3,4,*numbers))  #20 (элемента кортежа передались как кортеж необязательных аргументов)

numbers_dict = {"a":1, "b":2, "c":3, "d":4}
# print(summator(*numbers_dict))  # can only concatenate str (not "int") to str
# print(summator(**numbers_dict))  # 10 (значения словаря записались в позиционные аргументы)

# HARD
def summator_mod(a:int,b:int,c:int,d:int,*args:int,**kwargs):
    answer = a+b+c+d
    if args: 
        try:
            answer += sum(args[:2])
        except:
            answer += sum(args)
    if kwargs: answer += sum(kwargs.values())
    return answer

print(summator_mod(1,2,3,4))  # 10
print(summator_mod(1,2,3,4,5))  # 15
print(summator_mod(1,2,3,4,5,6,7,8))  # 21
print(summator_mod(1,2,3,4,5,6,e=10))  # 31
print(summator_mod(1,2,3,4,5,6,e=10,f=11))  # 42