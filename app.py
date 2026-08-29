import streamlit as st

from src.rag import executar_rag


st.title("RAG - HTTPX")

with st.form("pergunta_form"):
    pergunta = st.text_input("Digite sua pergunta:")

    enviar = st.form_submit_button("Perguntar")

if enviar:
    resultados, resposta = executar_rag(pergunta)

    st.write("CHUNKS ENCONTRADOS")

    for chunk in resultados:
        st.write(f"""**{chunk['chunk']['id']}
Score: {chunk['score']:.2f}
Arquivo: {chunk['chunk']['arquivo']}
Caminho: {chunk['chunk']['caminho']}**
{chunk['chunk']['texto']}
        """)
        st.divider()

    st.write("RESPOSTA")
    st.write(resposta[0])