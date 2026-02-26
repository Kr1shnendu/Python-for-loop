import logging
from typing import List, Set

logging.basicConfig(
    filename="missing-number.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def missing_number_in_list(nums: List[int]) -> int:
    """
    Find the missing number in a list containing numbers from 1 to N
    Parameters:
        nums (List[int]): Input list
    Returns:
        int: Missing number
    """

    nums: Set[int] = set(nums)
    n = len(nums) + 1
    missing_num = 0

    for i in range(1, n + 1):
        if i not in nums:
            missing_num = i
            break

    logging.info(f"Missing number in {nums} : {missing_num}")
    return missing_num


missing_number_in_list([1, 2, 3, 5, 6, 7])
missing_number_in_list([1, 2, 3, 4])
missing_number_in_list([2,])