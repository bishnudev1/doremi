import streamlit as st
from llm_helper import load_and_embed_documents, query_responses, process_llm_response

st.set_page_config(page_title="Doremi", page_icon="📚", layout="wide")

st.title("Doremi 📚")
st.write("An assistant tool for querying documents and getting intelligent responses.")

urls = st.text_area("Enter URLs (comma-separated)").split(',')

if st.button("Load URLs"):
    with st.spinner("Loading and embedding documents..."):
        db = load_and_embed_documents(urls)
        st.session_state['db'] = db
        st.success("Documents loaded & you can now query them.")

query = st.text_input("Enter your query")

if st.button("Get Answer"):
    if 'db' in st.session_state:
        with st.spinner("Retrieving answer..."):
            llm_response = query_responses(st.session_state['db'], query)
            wrapped_result = process_llm_response(llm_response)
            st.write("### Answer")
            st.write(wrapped_result)
            # st.write("### Sources")
            # st.write(sources)
    else:
        st.error("Please load and embed documents first.")

st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)
