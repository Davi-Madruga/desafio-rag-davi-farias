import streamlit as st

from src.rag import executar_rag


st.title("RAG - HTTPX")


with st.form("pergunta_form"):
    pergunta = st.text_input("Digite sua pergunta:")
    enviar = st.form_submit_button("Perguntar")


if enviar:
    with st.spinner("Carregando..."):
        resultados, resposta = executar_rag(pergunta)

    st.subheader("Resposta")
    st.write(resposta[0])

    if resposta[1]:
        st.subheader("Chunks encontrados")

        for chunk in resultados:
            with st.expander(
                f"{chunk['chunk']['id']} — Score: {chunk['score']:.2f}"
            ):
                st.write(f"**Arquivo:** {chunk['chunk']['arquivo']}")
                st.write(f"**Caminho:** {chunk['chunk']['caminho']}")
                st.write(chunk['chunk']['texto'])