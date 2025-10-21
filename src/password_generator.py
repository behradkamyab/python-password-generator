from abc import ABC, abstractmethod


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