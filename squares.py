"""Computation of weighted average of squares."""
import argparse


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares) / sum(effective_weights)

def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [int(number_string) for number_string in all_numbers]  # 修复：改为int



if __name__ == "__main__":
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='Calculate the weighted average of squares of numbers'
    )
    
    # 添加 numbers 参数
    parser.add_argument(
        'numbers',
        type=float,
        nargs='+',
        help='Numbers to calculate the average of their squares'
    )
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 使用解析的参数
    numbers = args.numbers
    weights = None  # 暂时保持权重硬编码为 None
           
    
    result = average_of_squares(numbers, weights)
    
    print(result)