import logging
from typing import List

logging.basicConfig(
    filename="remove-duplicates.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def remove_duplicates(nums: List[int]) -> List[int]:
    """
    Remove duplicate elements from a list while preserving order
    Parameters:
        nums (List[int]): Input list
    Returns:
        List[int]: List without duplicates in it
    """

    result_list = []
    for num in nums:
        if num not in result_list:
            result_list.append(num)

    logging.info(f"List after removing duplicates: {result_list}")
    return result_list


remove_duplicates([2, 4, 2, 5, 4, 2, 6, 4, 9])
remove_duplicates([10, 20, 32, 21, 21, 21, 10, 40])