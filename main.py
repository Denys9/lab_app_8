import random
def two():
    try:
        size = int(input('size - '))
        begin = int(input('begin - '))
        end = int(input('end - '))
        my_list = list()

        for i in range(size):
            my_list.append(random.randint(begin, end))
        print(f'{my_list}')

        odd = []
        even = []
        neg = []
        pos = []





    except Exception as ex:
        print(f'Eror information: {ex}')


two()