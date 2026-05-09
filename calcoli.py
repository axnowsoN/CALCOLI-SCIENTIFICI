import streamlit as st
import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calcoli scientifici", layout="centered")

st.title("Calcoli scientifici")

st.write("Mini app per fare conti simbolici, numerici e grafici.")

st.divider()

st.header("Calcolatrice simbolica")

espressione = st.text_input(
    "Inserisci un'espressione",
    value="1/3 + 1/6"
)

if st.button("Calcola espressione"):
    try:
        risultato = sm.sympify(espressione)

        st.subheader("Risultato simbolico")
        st.latex(sm.latex(risultato))

        st.subheader("Risultato numerico")
        st.write(risultato.evalf())

    except Exception as e:
        st.error("Errore nel calcolo.")
        st.write(e)

st.divider()

st.header("Calcolo energia del fotone")

st.latex(r"E = h\nu")
st.latex(r"\lambda = \frac{c}{\nu}")

h = 6.62607015e-34
c = 2.99792458e8

frequenza = st.number_input(
    "Frequenza ν in Hz",
    value=1.0e14,
    format="%.5e"
)

energia = h * frequenza
lunghezza_onda = c / frequenza

st.write(f"Energia: {energia:.5e} J")
st.write(f"Lunghezza d'onda: {lunghezza_onda:.5e} m")

st.divider()

st.header("Grafico funzione")

funzione = st.text_input(
    "Funzione f(x)",
    value="sin(x)"
)

x_min = st.number_input("x minimo", value=-10.0)
x_max = st.number_input("x massimo", value=10.0)

if st.button("Disegna grafico"):
    try:
        x = sm.Symbol("x")
        expr = sm.sympify(funzione)

        f = sm.lambdify(x, expr, "numpy")

        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = f(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title(f"Grafico di {funzione}")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error("Errore nel grafico.")
        st.write(e)