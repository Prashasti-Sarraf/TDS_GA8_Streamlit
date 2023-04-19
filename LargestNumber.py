import streamlit as st

def largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

st.title('Find the largest number among three')
st.write('Enter the three numbers below')
num1 = st.number_input('Number 1', min_value=0, step=1)
num2 = st.number_input('Number 2', min_value=0, step=1)
num3 = st.number_input('Number 3', min_value=0, step=1)

if st.button('Find Largest'):
    result = largest_number(num1, num2, num3)
    st.write(f'The largest number among {num1}, {num2}, and {num3} is: {result}')
