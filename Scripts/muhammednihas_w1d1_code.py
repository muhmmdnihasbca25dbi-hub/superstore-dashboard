import streamlit as st

st.title("muhammed nihas's Portfolio")

st.header("About Us")
st.write("""
I am a BCA student interested in AI, data analytics, and web development.
I enjoy learning new technologies and building creative projects.
""")


st.header("Skills",divider="light blue" )

st.markdown("- python\n- pandas \n- tableau \n- sql \n- html \n- css \n- js")

st.header("code",divider="light blue")
st.caption("source: muhammednihas_w1d1.csv")
st.code("df=pd.read_csv('data/muhammednihas_w1d1.csv')",language="python")
st.header("result",divider="light blue")
st.latex(r'\text{muhammednihas}=\frac{\text{muhammednihas}}{\text{muhammednihas}}')