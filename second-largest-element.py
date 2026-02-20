import logging
from typing import List

logging.basicConfig(
    filename="second-largest-element.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def second_largest_element(l: List[int]) -> int:
    """
    Finds the second largest elements in a list
    Parameters:
        l (List[int]): Input list of integers
    Returns:
        int: Second largest element
    """
    largest = l[0]
    for num in l:
        if(num>largest):
            largest = num
    
    sec_largest = -10000
    for num in l:
        if((num != largest) and (num > sec_largest)):
            sec_largest = num

    if(sec_largest == -10000):
        logging.warning(f"There is no second largest element in the list: {l}")
        return -1
    
    logging.info(f"The second largest elements in a list: {l} is: {sec_largest}")
    return sec_largest


second_largest_element([32, 32])
second_largest_element([2, 3, 7, 2, 9, 8, 6])
second_largest_element([2, 3, 7, 5])
second_largest_element([32, 71, 56, 87, 20])