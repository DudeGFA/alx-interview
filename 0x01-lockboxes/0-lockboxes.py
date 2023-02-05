#!/usr/bin/python3
"""
    Contains function canUnlockAll
"""


def recursiveUnlock(boxes, index, unlockableBoxes):
    for key in boxes[index]:
        if key < len(unlockableBoxes) and unlockableBoxes[key] == 0:
            unlockableBoxes[key] = 1
            unlockableBoxes = recursiveUnlock(boxes, key, unlockableBoxes)
    return unlockableBoxes


def canUnlockAll(boxes):
    """"
        Checks if all boxes in a list of list
        can be unlocked. The first box is unlocked
        A key with the same number as a box opens that box
        Args:
            boxes: A list of list
        Returns: True or False
    """
    unlockableBoxes = []
    for box in boxes:
        unlockableBoxes.append(0)
    unlockableBoxes[0] = 1
    for key in boxes[0]:
        if key < len(unlockableBoxes):
            unlockableBoxes[key] = 1
            unlockableBoxes = recursiveUnlock(boxes, key, unlockableBoxes)
    # for i in range(len(boxes)):
     #   for box in boxes:
      #      if unlockableBoxes[boxes.index(box)] == 1:
       #         for key in box:
        #            if key < len(unlockableBoxes):
         #               unlockableBoxes[key] = 1

    for key in unlockableBoxes:
        if key != 1:
            return False
    return True
