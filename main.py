import random
def one():
    try:
        size = int(input('size - '))
        begin = int(input('begin - '))
        end = int(input('end - '))
        my_list = list()
        neg = 0
        odd = []
        even = []
        mul_3 = 1
        start_1 = []
        end_1 = []

        for i in range(size):
            my_list.append(random.randint(begin,end))
        print(f'{my_list}')

        for i in my_list:
            if i < 0:
                neg += i
            if i%2 == 0:
                even.append(i)
            if i%2 !=0:
                odd.append(i)
        for i in range(3, len(my_list), 3):
            mul_3 *= my_list[i]


        print(f'sum neg = {neg}\nsum odd = {sum(odd)}\nsum even = {sum(even)}')
        print(f'mul even 3 index = {mul_3}')
        print(f'')


    except Exception as ex:
            print(f'Eror information: {ex}')


one()