import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.title("🧠 Advanced Math Streamlit App")

# User input for symbolic equation solving
st.header("1. Symbolic Equation Solver")
equation_input = st.text_input("Enter an equation (e.g., x**2 - 4 = 0):", value="x**2 - 4 = 0")

x = sp.Symbol('x')
if equation_input:
    try:
        eq = sp.sympify(equation_input.split('=')[0]) - sp.sympify(equation_input.split('=')[1])
        solutions = sp.solve(eq, x)
        st.write("✅ Solutions:", solutions)
    except Exception as e:
        st.error(f"❌ Error parsing equation: {e}")

# Plot a math function
st.header("2. Function Plotter")
func_input = st.text_input("Enter a function of x (e.g., sin(x), x**2, exp(-x)):", value="x**2")

if func_input:
    try:
        func = sp.lambdify(x, sp.sympify(func_input), "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_title(f"Plot of {func_input}")
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"❌ Could not plot function: {e}")

# Calculator
st.header("3. Calculator")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "∞"
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error during calculation: {e}")
