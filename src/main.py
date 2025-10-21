from pin_password_generator import PinPasswordGenerator
from random_password_generator import RandomPasswordGenerator
from memorable_password_generator import MemorablePasswordGenerator

def main():
    """
    Main function to demonstrate the usage of all password generators.
    """
    # Create and use a PinPasswordGenerator object
    pin_gen = PinPasswordGenerator(8)
    print("Generated PIN:", pin_gen.generate())
    
    # Create and use a RandomPasswordGenerator object
    random_gen = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
    print("Generated Random Password:", random_gen.generate())
    
    # Create and use a MemorablePasswordGenerator object
    # Note: nltk.download('words') must be run first in a terminal
    memorable_gen = MemorablePasswordGenerator(num_of_words=5, capitalize=True , vocabulary=['my' , 'bnehrad' , 'sdfsd' , 'dsdsdsdsdsdsdsdsdsdsds'])
    print("Generated Memorable Password:", memorable_gen.generate())
if __name__ == '__main__':
    main()