def sort_tuple(nested_list):
    u"""
    Sort list of tuple base on the first element in the tuple
    docs: https://docs.python.org/3/howto/sorting.html

    :param nested_list:
    :return:

    >>> sort_tuple([[88,332], [1, 34], [0, 45], [-44, 33], [99, 455]])
    [[-44, 33], [0, 45], [1, 34], [88, 332], [99, 455]]

    >>> sort_tuple([[1, 2], [2, 34], [3, 45], [4, 33], [5, 455]])
    [[1, 2], [2, 34], [3, 45], [4, 33], [5, 455]]
    """

    return sorted(nested_list, key=lambda x: x[0])


def get_biggest_item(first, second):
    # TODO complete docu
    u"""

    :param first:
    :param second:
    :return:

    >>> get_biggest_item(123, 3222)
    3222

    >>> get_biggest_item(3222, 123)
    3222
    """
    return max(first, second)


def merge(raw_list):
    u""""

    # TODO complete docu
    :param raw_list:
    :return:
    """

    sorted_list = sort_tuple(raw_list)
    result = [sorted_list[0]]

    for interval in sorted_list:
        previous = result[-1]
        if interval[0] <= previous[1]:
            previous[1] = get_biggest_item(previous[1], interval[1])
        else:
            result.append(interval)

    return result


if __name__ == '__main__':
    raw = merge([[25, 30], [2, 19], [14, 23], [4, 8]])
    print(sort_tuple(raw))
