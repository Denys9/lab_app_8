import random
def two():
    try:
        size = int(input('size - '))
        begin = int(input('begin - '))
        end = int(input('end - '))
        my_list = list()
        for i in range(size):
            my_list.append(random.randint(begin, end))
        print(f'full list = {my_list}')
        odd = []
        even = []
        neg = []
        pos = []
        for i in my_list:
            if i < 0:
                neg.append(i)
            if i%2 == 0:
                even.append(i)
            if i%2 !=0:
                odd.append(i)
            if i > 0:
                pos.append(i)
        print(f'odd = {odd}')
        print(f'even = {even}')
        print(f'negative = {neg}')
        print(f'positive = {pos}')
    except Exception as ex:
        print(f'Eror information: {ex}')


two()