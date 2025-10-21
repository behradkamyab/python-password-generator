import streamlit as st
from password_generators import PinPasswordGenerator, RandomPasswordGenerator , MemorablePasswordGenerator

st.title(":zap: Password Generator")


option = st.radio("Select which type of password you want: ",['Random' , 'Memorable' , 'Pin Code'],)

if option == "Pin Code":
    length = st.slider("Enter the length of the Pin Code" , min_value=6 , max_value=32)
    generator = PinPasswordGenerator(length)
elif option == "Random":
    length = st.slider("Enter the length of the Random password" , min_value=8 , max_value=32)
    include_numbers = st.toggle('Include Numbers')
    include_symbols = st.toggle('Include Symbols')
    generator = RandomPasswordGenerator(length,include_numbers,include_symbols)
elif option == "Memorable":
    length = st.slider("Enter the number of words" , min_value=4 , max_value=32)
    is_capitalized = st.toggle('Capitalize')
    separator = st.text_input('Separator' , value='-')
    include_numbers = st.toggle('Include Numbers')
    include_symbols = st.toggle('Include Symbols')
    generator = MemorablePasswordGenerator(length,is_capitalized,include_numbers,include_symbols)


password = generator.generate()
st.write(f"Your password is: `{password}`")