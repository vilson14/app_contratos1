import streamlit as st
import pandas as pd
import numpy as np

st.title("Contratos em aberto")

st.header ("Bancos")

st.sidebar.title("Paticipantes")


operacao = st.sidebar.radio('Escolha:', ['Estrangeiro', 'Bancos','Fundos' ,'CPF',])




chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)




chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)