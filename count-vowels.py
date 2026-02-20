import logging

logging.basicConfig(
    filename="count-vowels.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string
    Parameters:
        s (str): Input string
    Returns:
        int: No of vowels
    """
    vowels = "aeiou"
    count = 0
    for ch in s:
        if(ch.lower() in vowels):
            count+=1

    logging.info(f"number of vowels in '{s}' are: {count}")
    return count


n1 = count_vowels("agfseio")
n2 = count_vowels("hello")
n2 = count_vowels("python")