import random
import string
from abc import ABC, abstractmethod

import nltk



class PasswordGenerator(ABC):
    """
    An abstract base class for all password generator types.

    This class serves as a blueprint, enforcing a common interface
    for all password generator subclasses. All subclasses must
    implement the 'generate' method.
    """
    
    @abstractmethod
    def generate(self) -> str:
        """
        Generates a password.

        This method must be implemented by any concrete subclass.
        The specific generation logic depends on the subclass.

        Returns:
            str: The generated password.
        """
        pass
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
    





class MemorablePasswordGenerator(PasswordGenerator):
    """
    Generates a memorable password by combining words from a vocabulary.

    This class creates a password by joining multiple words with a separator.
    Options for capitalization and a custom vocabulary are available.
    """
    def __init__(self, num_of_words: int =4 , capitalize: bool =False , separator: str ='-', vocabulary: list = None):
        """
        Initializes the MemorablePasswordGenerator.

        Args:
            num_of_words (int): The number of words to use in the password. Defaults to 4.
                                Must be at least 4.
            capitalize (bool): Whether to randomly capitalize words. Defaults to False.
            separator (str): The character(s) used to join the words. Defaults to '-'.
            vocabulary (list, optional): A list of words to use. If None, uses nltk's corpus.

        Raises:
            ValueError: If the number of words is less than 4.
        """
        if not 4 <= num_of_words:
            raise ValueError("Number of words must be at least 4 words.")
        self.num_of_words = num_of_words
        self.capitalize = capitalize
        self.separator = separator
        if vocabulary is None:
            # Download the words corpus quietly and only if it's not already installed
            try:
                self.vocabulary = nltk.corpus.words.words()
            except LookupError:
                print("NLTK 'words' corpus not found. Downloading...")
                nltk.download('words')
                self.vocabulary = nltk.corpus.words.words()
        else:
            self.vocabulary = vocabulary
    def generate(self):
        """
        Generates a memorable password based on words from the vocabulary.

        Returns:
            str: The generated password.
        """
        words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            words = [word.upper() if random.choice([True,False]) else word.lower() for word in words]
        return self.separator.join(words)
