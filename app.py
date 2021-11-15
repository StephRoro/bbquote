import streamlit as st

from bbquote.lib import get_quote

st.write(get_quote())
