from binary_search import binary_search_recursive, binary_search

def checking_for_equal(a, b):
    if a == b:
        print('OK! {} == {}'.format(a, b))
    else:
        print('Error! {} != {}'.format(a, b))



if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    b_1 = binary_search(a, 8)
    b_2 = binary_search_recursive(a, 8, 0, len(a))
    checking_for_equal(b_1, b_2)

