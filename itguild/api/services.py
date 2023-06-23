def markopolo(num):
    if num % 2 == 0 and num % 3 == 0:
        return 'МаркоПолло'
    elif num % 2 == 0:
        return 'Марко'
    elif num % 3 == 0:
        return 'Полло'
    else:
        return num