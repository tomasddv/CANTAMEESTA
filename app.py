from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='¡Cantá esa palabra!', page_icon='🎵', layout='centered', initial_sidebar_state='collapsed')
st.markdown('''<style>
[data-testid="stHeader"], [data-testid="stToolbar"] {display:none}
.block-container {padding:0 !important; max-width:100% !important}
[data-testid="stAppViewContainer"] {background:#120d20}
iframe {display:block; border:0 !important;}
</style>''', unsafe_allow_html=True)
html = (Path(__file__).parent / 'cancion_con_la_palabra.html').read_text(encoding='utf-8')
components.html(html, height=1050, scrolling=True)
