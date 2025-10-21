from password_generator import PasswordGenerator
import random
import nltk




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
