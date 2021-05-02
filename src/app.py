import time
import logging
import sys
import json


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def sort_tuple(nested_list):
    # type: (List[Tuple[float|int, float|int]]) -> List[Tuple[float|int, float|int]]
    u"""
    Sort list of tuple base on the first element in the tuple
    docs: https://docs.python.org/3/howto/sorting.html

    >>> sort_tuple([[88,332], [1, 34], [0, 45], [-44, 33], [99, 455]])
    [[-44, 33], [0, 45], [1, 34], [88, 332], [99, 455]]

    >>> sort_tuple([[1, 2], [2, 34], [3, 45], [4, 33], [5, 455]])
    [[1, 2], [2, 34], [3, 45], [4, 33], [5, 455]]
    """

    return sorted(nested_list, key=lambda x: x[0])


def get_biggest_item(first, second):
    # type: (float|int, float|int) -> float|int
    u"""
    Returns the highest number between two

    >>> get_biggest_item(123, 3222)
    3222

    >>> get_biggest_item(3222, 123)
    3222

    >>> get_biggest_item(-123, -32)
    -32
    """
    return max(first, second)


def validate_input(input_list):
    """

    >>> validate_input([1,2,3])
    False

    >>> validate_input([[1,2,3]])
    False

    >>> validate_input([])
    False

    >>> validate_input([[1,3], [12, 9]])
    False

    >>> validate_input([[1,3], [12, "33"]])
    False

    >>> validate_input([[1,3]])
    True

    >>> validate_input([[25, 30], [2, 19], [14, 23], [4, 8]])
    True

    """
    result = all(isinstance(interval, list) for interval in input_list) and \
             all(isinstance(interval, list) for interval in input_list) and \
             all(isinstance(limit, (int, float)) for interval in input_list for limit in interval) and \
             len(input_list) > 0

    if not result:
        return False
    else:

        for interval in input_list:
            if len(interval) != 2 or interval[0] > interval[1]:
                return False

        return True


def merge(intervals):
    """"
    :type intervals: list of interval as List[Tuple[float|int, float|int]]) to be overlapped
    :rtype: overlapped interval as List[Tuple[float|int, float|int]] or TypeError: Invalid input

    The MERGE function, which takes a list of intervals and returns a list of intervals as a result.

    >>> merge([[25, 30], [2, 19], [14, 23], [4, 8]])
    [[2, 23], [25, 30]]

    >>> merge([])
    Traceback (most recent call last):
    ...
    TypeError: Invalid input
    """

    if not validate_input(intervals):
        raise TypeError("Invalid input")

    # record the time start
    start = time.time()
    # ordering the intervals on the smallest of the ranges.
    sorted_list = sort_tuple(intervals)

    # start the result list with the earliest interval(smallest) from which the others will overlap.
    result = [sorted_list[0]]

    # if the start of next interval is smaller than the end current list then overlaps otherwise push the interval
    for interval in sorted_list:
        previous = result[-1]
        if interval[0] <= previous[1]:

            # overlapping
            previous[1] = get_biggest_item(previous[1], interval[1])
        else:
            result.append(interval)

    # record the time end
    end = time.time()

    logger.info("the function takes {} ms".format(end-start))
    return result


if __name__ == '__main__':
    user_input = sys.argv[1:]
    try:
        user_input = [json.loads(i) for i in user_input]
        print(merge(user_input))

    except ValueError:
        raise TypeError("Invalid input")
