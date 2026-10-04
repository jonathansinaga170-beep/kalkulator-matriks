import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Kalkulator Operasi Matriks",
    page_icon="🔢",
    layout="wide"
)

st.title("🔢 Kalkulator Perkalian & Operasi Matriks")
st.caption("Aplikasi operasi matriks A (2×3) × B (3×2) → AB (2×2)")

# -----------------------------
# Input matriks
# -----------------------------
st.subheader("1. Input Matriks")

col_a, col_b, col_ab = st.columns([1, 0.25, 1])

default_a = np.array([[2, 1, 3], [4, 0, 2]], dtype=float)
default_b = np.array([[5, 2], [1, 4], [3, 7]], dtype=float)

with col_a:
    st.markdown("### Matriks A (2×3)")
    a1, a2, a3 = st.columns(3)
    with a1:
        a11 = st.number_input("A₁₁", value=2.0, key="a11")
        a21 = st.number_input("A₂₁", value=4.0, key="a21")
    with a2:
        a12 = st.number_input("A₁₂", value=1.0, key="a12")
        a22 = st.number_input("A₂₂", value=0.0, key="a22")
    with a3:
        a13 = st.number_input("A₁₃", value=3.0, key="a13")
        a23 = st.number_input("A₂₃", value=2.0, key="a23")

    A = np.array([[a11, a12, a13], [a21, a22, a23]], dtype=float)
    st.write("**A =**")
    st.dataframe(A, hide_index=True, use_container_width=True)

with col_b:
    st.markdown("### ×")

with col_ab:
    st.markdown("### Matriks B (3×2)")
    b1, b2 = st.columns(2)
    with b1:
        b11 = st.number_input("B₁₁", value=5.0, key="b11")
        b21 = st.number_input("B₂₁", value=1.0, key="b21")
        b31 = st.number_input("B₃₁", value=3.0, key="b31")
    with b2:
        b12 = st.number_input("B₁₂", value=2.0, key="b12")
        b22 = st.number_input("B₂₂", value=4.0, key="b22")
        b32 = st.number_input("B₃₂", value=7.0, key="b32")

    B = np.array([[b11, b12], [b21, b22], [b31, b32]], dtype=float)
    st.write("**B =**")
    st.dataframe(B, hide_index=True, use_container_width=True)

# -----------------------------
# Perkalian matriks
# -----------------------------
AB = A @ B

st.divider()
st.subheader("2. Hasil Perkalian Matriks")

c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### AB = A × B")
    st.dataframe(AB, hide_index=True, use_container_width=True)

with c2:
    st.markdown("### Bentuk Matriks")
    st.latex(
        r"AB =
        \begin{bmatrix}"
        + f"{AB[0,0]:.2f} & {AB[0,1]:.2f} \\\\ "
        + f"{AB[1,0]:.2f} & {AB[1,1]:.2f}"
        + r"\end{bmatrix}"
    )

# -----------------------------
# Detail perhitungan
# -----------------------------
st.divider()
st.subheader("3. Detail Perhitungan")

selected_row = st.selectbox("Pilih baris matriks A", [1, 2], index=0)
selected_col = st.selectbox("Pilih kolom matriks B", [1, 2], index=0)

r = selected_row - 1
c = selected_col - 1

terms = [
    f"({A[r,0]:g} × {B[0,c]:g})",
    f"({A[r,1]:g} × {B[1,c]:g})",
    f"({A[r,2]:g} × {B[2,c]:g})"
]

detail = " + ".join(terms)
st.info(f"(AB)₍{selected_row}{selected_col}₎ = {detail} = {AB[r,c]:g}")

# -----------------------------
# Semua elemen AB
# -----------------------------
st.markdown("### Semua langkah perhitungan")

for i in range(2):
    for j in range(2):
        expression = (
            f"(AB)₍{i+1}{j+1}₎ = "
            f"({A[i,0]:g} × {B[0,j]:g}) + "
            f"({A[i,1]:g} × {B[1,j]:g}) + "
            f"({A[i,2]:g} × {B[2,j]:g}) = {AB[i,j]:g}"
        )
        st.write(expression)

# -----------------------------
# Operasi tambahan
# -----------------------------
st.divider()
st.subheader("4. Operasi Matriks Persegi Tambahan")

det = np.linalg.det(AB)
rank = np.linalg.matrix_rank(AB)

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Det(AB)", f"{det:g}")
with m2:
    st.metric("Rank(AB)", str(rank))
with m3:
    if np.isclose(det, 0):
        st.metric("Invers", "Tidak ada")
    else:
        st.metric("Invers", "Tersedia")

if np.isclose(det, 0):
    st.warning("AB singular, sehingga tidak mempunyai invers.")
else:
    inv = np.linalg.inv(AB)
    st.markdown("### Invers AB")
    st.dataframe(
        np.round(inv, 2),
        hide_index=True,
        use_container_width=True
    )

st.divider()
st.caption("Kalkulator Operasi Matriks — A(2×3) × B(3×2) = AB(2×2)")
