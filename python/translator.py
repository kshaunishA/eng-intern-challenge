import sys

# Braille to alphabet mapping
braille_to_alphabet = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z"
}

# Braille to number mapping (same patterns as 'a' to 'j' but in number mode)
braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7",
    "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Alphabet to Braille mapping
alphabet_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}

# Numbers to Braille mapping (same pattern as above but reverse)
number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Special Braille markers
capital_follows = ".....O"  # Capital letter marker
number_follows = ".O.OOO"   # Number follows marker
space_braille = "......"    # Braille for space

def is_braille(input_str):
    # Check if input is likely Braille (consists only of O's and .'s)
    return all(c in "O." for c in input_str)

def braille_to_text(braille_str):
    result = []
    is_capital = False
    is_number = False
    
    # Process each 6-character chunk (representing a Braille character)
    for i in range(0, len(braille_str), 6):
        symbol = braille_str[i:i+6]
        if symbol == space_braille:
            result.append(" ")
            is_number = False  # Reset number mode after a space
            continue
        if symbol == capital_follows:
            is_capital = True
            continue
        if symbol == number_follows:
            is_number = True
            continue
        # Determine if it's number mode or alphabet mode
        if is_number:
            if symbol in braille_to_number:
                result.append(braille_to_number[symbol])
        else:
            if symbol in braille_to_alphabet:
                char = braille_to_alphabet[symbol]
                if is_capital:
                    char = char.upper()
                    is_capital = False
                result.append(char)
    
    return "".join(result).strip()  # Return result without trailing spaces

def text_to_braille(text_str):
    result = []
    is_number = False
    words = text_str.split()  # Split text into words
    for word in words:
        for char in word:
            if char.isdigit():
                if not is_number:
                    result.append(number_follows)  # Add number marker before first digit
                    is_number = True
                result.append(number_to_braille[char])
            elif char.isalpha():
                if is_number:
                    is_number = False  # End number mode when switching back to letters
                if char.isupper():
                    result.append(capital_follows)  # Add capital marker before uppercase letter
                result.append(alphabet_to_braille[char.lower()])
        result.append(space_braille)  # Add space after each word
    return "".join(result).strip(space_braille)  # Strip trailing space

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    input_str = sys.argv[1]
    
    if is_braille(input_str):
        translated = braille_to_text(input_str)
    else:
        translated = text_to_braille(input_str)
    
    print(translated)

if __name__ == "__main__":
    main()

