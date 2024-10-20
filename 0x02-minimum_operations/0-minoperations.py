#!/usr/bin/python3
'''This is a challenge on computing Minimum Operations'''


def minOperations(n):
    '''computes the min. num of events/operations
    required to fulfil exactly n H
    characters in a given file.
    Returns:
        Integer, on success
    Else:
        return 0 - min. operation not possible to attain
    '''
    chars_num = 1  # The number of characters in the argv file
    clipboard = 0  # The num of H in clipboard
    iterative_counter = 0  # Operations iterative counter

    while chars_num < n:
        # Check if nothing is copied yet.
        if clipboard == 0:
            # copy all
            clipboard = chars_num
            # Operation performed: increment iterative_counter
            iterative_counter += 1

        # Check if nothing is pasted yet
        if chars_num == 1:
            # paste clipboard content
            chars_num += clipboard
            # Operation performed: increment iterative_counter
            iterative_counter += 1
            # continue to next loop
            continue

        remainder = n - chars_num  # remainder characters to paste
        # Check for impossible operation by:
        # checking if clipboard has more than needed
        # or more than in the clipboard.
        # In either case:
        # it's impossible to achieve n of chars
        if remainder < clipboard:
            return 0

        # if division has remainder
        if remainder % chars_num != 0:
            # paste current clipboard content
            chars_num += clipboard
            # Operation performed: increment iterative_counter
            iterative_counter += 1
        else:
            # copy all
            clipboard = chars_num
            # and paste
            chars_num += clipboard
            # Operation performed: increment iterative_counter
            iterative_counter += 2

    # if min. operation is achievable
    if chars_num == n:
        return iterative_counter
    else:
        return 0
