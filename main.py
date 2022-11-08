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

        mul = 1
        minn = my_list.index(min(my_list))
        maxx = my_list.index(max(my_list))
        if minn > maxx:
            minn, maxx = maxx, minn
        for i in range(minn, maxx+1):
            mul *= my_list[i]

        start = end = 0
        mul3 = 1
        for i in range(0, len(my_list)):
            if start > my_list[i] > 0:
                start = i
            if end < my_list[i] > 0:
                end = i
        if start > end:
            start, end = end, start
        for i in range(start+1, end):
            mul3 += my_list[i]
        print(my_list[i])
        print(f'mul = {mul}')
        print(f'sum neg = {neg}\nsum odd = {sum(odd)}\nsum even = {sum(even)}')
        print(f'mul even 3 index = {mul_3}')

    except Exception as ex:
        print(f'Eror information: {ex}')


one()