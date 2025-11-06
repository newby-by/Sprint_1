"""The task7
"""
MAX_VALUE = 10e7


def digit_root(num):
    if not isinstance(num, int):
        raise ValueError(f'{num}, the integer is allowed only.')
    if num > MAX_VALUE:
        raise ValueError(f'{num} is more than {int(MAX_VALUE)}.')

    while len(list(str(num))) != 1: 
        numbers = list(str(num))
        num = sum(map(int, numbers))

    return num


if __name__ == '__main__':
    # print(digit_root(12333.0))
    # print(digit_root(100000000000000000000000000000000))
    assert digit_root(4851) == 9
    assert digit_root(97569) == 9
    assert digit_root(889987) == 4
