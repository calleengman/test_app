import streamlit as st
import pandas as pd

ANSWER = 'ADIEU'

class Wordle():
    def __init__(self):
        self.answer = 'ADIEU'
        self.guesses = []

    def checkGuess(self,word):
        self.guesses.append(word)
        if word == self.answer:
            return True

def list_to_df(list):
    list_of_lists = []
    for item in list:
        list_of_lists.append([i for i in item])
    return pd.DataFrame(list_of_lists)

def check_guess(guess,answer):
    points = [0,0,0,0,0]
    for i,letter in enumerate(guess):
        if letter == answer[i]:
            points[i] = 2
        elif letter in answer:
            points[i] = 1
    return points

def colormap(x):
    if x == 2:
        return 'background-color: green'
    elif x == 1:
        return 'background-color: yellow'
    else:
        return 'background-color: grey'
    

def main():
    st.title('Streamlit App')
    if 'guesses' not in st.session_state:
        st.session_state['guesses'] = []
    if 'points' not in st.session_state:
        st.session_state['points'] = []
    guess = st.text_input('Enter a guess').upper()
    if len(st.session_state['guesses'])<6 and len(guess) == 5:
        st.session_state['guesses'].append(guess)
        st.session_state['points'].append(check_guess(guess,ANSWER))
    else:
        st.write('Guess must be 5 letters')
    # st.write('Guesses: ', st.session_state['guesses'])
    # st.write('Points: ', st.session_state['points'])
    df = list_to_df(st.session_state['guesses'])
    df_points = list_to_df(st.session_state['points'])
    # df_points = df_points.style.applymap(colormap)
    df = df.style.apply(lambda x: df_points.applymap(colormap), axis=None)

    st.dataframe(df)
    # st.dataframe(df_points)
    if st.session_state['guesses'][-1] == ANSWER:
        st.write('You Win!')
    elif len(st.session_state['guesses']) == 6:
        st.write('You Lose!')


main()