from itertools import zip_longest, \
                      islice


def nums_gener(max_num):
    for num in range(1, max_num+1,2):
        yield num **2

nums_gen = nums_gener(10**6)
print(sum(nums_gen))



def odd_nums(num):
    for i in range(1, num+1,2):
        yield
odd = odd_nums(15)
print(next(odd))
print(odd_nums(15))



tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '1M','1N'
]

mix_list = [el for el in zip_longest(tutors, klasses)]
print (mix_list)



src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]


#src_itr = list(map(lambda x: x<, src))
src_result = []
for i, j in zip(src,src[1::]):
    if i<j:
        src_result.append(j)


#src_result = [el for el in src if el < next(islice(src,None,None,None))]
# print(type(src_result))
# print(next(src_result))
# print(next(src_result))
print(src_result)

Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]


Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
