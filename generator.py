def markopolo(num):
    if num is str and not num.isdigit():
        return 'Необходимо число'
    num = int(num)
    if num % 2 == 0 and num % 3 == 0:
        return 'МаркоПолло'
    elif num % 2 == 0:
        return 'Марко'
    elif num % 3 == 0:
        return 'Полло'
    else:
        return num

def markopolo_gen():
    for num in range(1001):
        if num % 2 == 0 and num % 3 == 0:
            yield 'МаркоПолло'
        elif num % 2 == 0:
            yield 'Марко'
        elif num % 3 == 0:
            yield 'Полло'
        else:
            yield num


print([i for i in markopolo_gen()])
