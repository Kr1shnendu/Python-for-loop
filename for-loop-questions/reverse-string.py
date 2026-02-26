import logging

logging.basicConfig(
    filename="reverse-string.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    filemode='a'
)

def reverse_string(s: str) -> str:
    """
    Reverse a string using a for loop (no slicing).
    Parameters:
        s (str): Input string
    Returns:
        str: Reversed string
    """

    rev_str = ""
    for ch in s:
        rev_str = ch + rev_str

    logging.info(f"Reversed string of {s} : {rev_str}")

    return rev_str


reverse_string("krishnendu")
reverse_string("hello world")
reverse_string("python")