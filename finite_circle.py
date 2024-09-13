import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime

st.title("Unit Circle over Finite Fields Visualization")

# Slider for selecting prime number p

p = st.slider("Select a prime number p (greater than 2):", value = (3,5,7,11,13,17,19,23,29))
#p = st.slider("Select a prime number p (greater than 2):", min_value=3, max_value=29, step=1)

# Ensure p is prime
if not isprime(p):
    st.warning(f"{p} is not a prime number. Please select a prime number.")
    st.stop()

# Slider for selecting number of multiples to draw
n_multiples = st.slider("Select the number of multiples to draw:", min_value=1, max_value=50, step=1)

# Generate all pairs (x, y) satisfying x^2 + y^2 ≡ 1 mod p
points = []
for x in range(p):
    for y in range(p):
        if (x**2 + y**2) % p == 1 % p:
            points.append((x, y))

# Define complex multiplication modulo p
def complex_mult(a, b):
    (x1, y1) = a
    (x2, y2) = b
    x = (x1 * x2 - y1 * y2) % p
    y = (x1 * y2 + x2 * y1) % p
    return (x, y)

# Define function to compute powers of an element
def compute_powers(g, n):
    powers = []
    current = g
    for _ in range(n):
        powers.append(current)
        current = complex_mult(current, g)
    return powers

# Find generators with their orders
def find_generators(points):
    generators = []
    identity = (1 % p, 0 % p)
    for g in points:
        seen = set()
        current = g
        order = 1
        while True:
            if current in seen:
                break
            seen.add(current)
            current = complex_mult(current, g)
            order += 1
            if current == identity:
                break
        if order == len(points):
            generators.append((g, order))
    return generators

# Find the generator with least positive x
generators = find_generators(points)
if not generators:
    st.warning("No generator found for this prime number.")
    st.stop()

generators.sort(key=lambda item: (item[0][0], item[0][1]))
generator = generators[0][0]
st.write(f"Generator chosen: {generator}")

# Compute multiples of the generator
multiples = compute_powers(generator, n_multiples)

# Prepare data for plotting
x_vals = [x for x, y in points]
y_vals = [y for x, y in points]
gen_x_vals = [x for x, y in multiples]
gen_y_vals = [y for x, y in multiples]

# Plotting
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, color='lightgray', label='Unit Circle Points')
ax.scatter(gen_x_vals, gen_y_vals, color='blue', label='Multiples of Generator')

# Annotate the multiples with positive integers
for idx, (x, y) in enumerate(multiples, 1):
    ax.text(x, y, str(idx), color='red', fontsize=12)

ax.set_title(f"Unit Circle over Finite Field with p = {p}")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

st.pyplot(fig)

