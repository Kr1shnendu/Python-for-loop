import logging

logging.basicConfig(
    filename="character-frequency.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def freq(s: str) -> dict:
    """
    Print the frequency of each character in a string
    Parameters:
        s (str): Input string
    Returns:
        dict: No of vowels
    """
    d = {}

    for ch in s:
        d[ch] = 0

    for ch in s:
        d[ch] = d[ch] + 1
    
    logging.info(f"frequency of characters in {s} is: {d}")
    return d

freq("helloworld")
freq("krishnendu")