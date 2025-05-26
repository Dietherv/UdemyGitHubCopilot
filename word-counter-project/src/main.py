def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text.replace(" ", "").replace("\t", "").replace("\n", ""))

def classify_even_odd(number):
    """
    Clasifica si un número es par o impar.

    Args:
        number (int): El número a clasificar.

    Returns:
        str: "par" si el número es par, "impar" si es impar.
    """
    return "par" if number % 2 == 0 else "impar"

if __name__ == "__main__":
    text_input = input("Please enter the text: ")
    word_count = count_words(text_input)
    char_count = count_characters(text_input)
    print(f"The number of words in the input text is: {word_count}")
    print(f"The number of characters (excluding whitespace) is: {char_count}")