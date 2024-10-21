#!/usr/bin/python3
'''ALX Backend Interview Challenge: LockBoxes'''


def canUnlockAll(boxes):
    '''Function det. if all the boxes can be opened by a key or not
    Expected Method Outcomes:
        Return True: all boxes can be opened
        Return False: not all boxes can be opened
    '''
    list_len = len(boxes)
    found_keys = set()
    opened_boxes = []
    key_pos = 0

    while key_pos < list_len:
        # Search for keys
        prev_key_pos = key_pos
        opened_boxes.append(key_pos)
        found_keys.update(boxes[key_pos])
        for key in found_keys:
            # Use key found to attempt to open boxes
            if key != 0 and key < list_len and key not in opened_boxes:
                key_pos = key
                break
        if prev_key_pos != key_pos:
            continue
        else:
            break

    for key_pos in range(list_len):
        # If no keys are found
        if key_pos not in opened_boxes and key_pos != 0:
            return False
    return True
