def binary_search(array, target):
    '''
    Usual binary search algorithm               --- Обычный алгоритм бинарного поиска
    To check if an element is inside an array   --- Для проверки на нахождение элемента внутри массива
    :param array:
    Ascending sorted array                      --- Отсортированный по возрастанию массив
    :param target:
    Search target - number                      --- Цель поиска - число
    :return:
    Search target index in array                --- Индекс цели поиска в массиве
    or None                                     --- или None
    '''
    left, right = (0, len(array)-1)
    while left <= right:
        mid = (left+right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None

def binary_search_recursive(array, target, left, right):
    '''
        Recursive binary search algorithm           --- Рекурсивный алгоритм бинарного поиска
        To check if an element is inside an array   --- Для проверки на нахождение элемента внутри массива
        :param array:
        Ascending sorted array                      --- Отсортированный по возрастанию массив
        :param target:
        Search target - number                      --- Цель поиска - число
        :param left:
        Left search border                          --- Левая граница поиска
        :param right:
        Right search border                         --- Правая граница поиска
        :return:
        Search target index in array                --- Индекс цели поиска в массиве
        or None                                     --- или None
    '''
    if left > right:
        return None
    mid = (left+right) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search_recursive(array, target, left, mid-1)
    else:
        return binary_search_recursive(array, target, mid+1, right)



