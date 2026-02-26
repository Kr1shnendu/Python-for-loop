import logging
from typing import List

logging.basicConfig(
    filename="check-sorted.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def check_sorted(l: List[int]) -> int:
    """
    Checks whether a list is sorted in ascending order
    Parameters:
        l (List[int]): Input list of integers
    Returns:
        bool: True, if the list is sorted in ascending order. Otherwise, False
    """
    copy_l = l.copy()
    copy_l.sort()
    if(l == copy_l):
        logging.info(f"The list: {l} is sorted in ascending order")
        return True
    else:
        logging.info(f"The list: {l} is not sorted ascending order")
        return False

check_sorted([2, 3, 7, 2, 9, 8, 6])
check_sorted([2, 3, 5, 8])
check_sorted([7, 5, 2])