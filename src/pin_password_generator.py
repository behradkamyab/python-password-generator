from password_generator import PasswordGenerator
import string
import random

class PinPasswordGenerator(PasswordGenerator):
    """
    Generates a password consisting of only numeric digits (a PIN).

    This class generates a password by randomly choosing digits
    from '0' to '9' for a specified length.
    """
    def __init__(self , length: int):
        """
        Initializes the PinPasswordGenerator.

        Args:
            length (int): The desired length of the PIN.
                          Must be between 6 and 100 characters.

        Raises:
            ValueError: If the length is not within the valid range.
        """
        if not 6 <= length <= 100:
            raise ValueError("The length must be at least 6 and at most 100 characters.")
        self.length = length
        
    def generate(self) -> str :
        """
        Generates a PIN of the specified length.

        Returns:
            str: The generated PIN.
        """
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
        