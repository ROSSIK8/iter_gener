# 1
class FlatIterator:

    def __init__(self, list_of_lists):
        self.list = []
        for list_ in list_of_lists:
            for item in list_:
                self.list.append(item)


    def __iter__(self):
        return self

    def __next__(self):
        if not self.list:
            raise StopIteration
        return self.list.pop(0)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        print(flat_iterator_item)

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
