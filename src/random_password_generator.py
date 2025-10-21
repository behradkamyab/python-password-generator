from password_generator import PasswordGenerator
import string
import random

class RandomPasswordGenerator(PasswordGenerator):
    """
    Generates a random password from a combination of letters, numbers, and symbols.

    The password's character set is configurable based on the initialization arguments.
    """
    def __init__(self, length: int =8 , include_numbers: bool =False , include_symbols: bool =False):
        """
        Initializes the RandomPasswordGenerator.

        Args:
            length (int): The desired length of the password. Defaults to 8.
                          Must be between 8 and 100 characters.
            include_numbers (bool): Whether to include numbers in the character set. Defaults to False.
            include_symbols (bool): Whether to include symbols in the character set. Defaults to False.

        Raises:
            ValueError: If the length is not within the valid range.
        """
        if not 8 <= length <= 100:
            raise ValueError("The length of the password must be at least 8 and at most 100 characters.")
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
           self.characters += string.digits
        if include_symbols:
           self.characters += string.punctuation
    def generate(self):
        """
        Generates a random password from the configured character set.

        Returns:
            str: The generated random password.
        """
        return ''.join([random.choice(self.characters) for _ in range(self.length)])