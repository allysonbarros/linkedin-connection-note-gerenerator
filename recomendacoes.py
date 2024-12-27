import os
import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

def generate_recommendation(nome, relacao_profissional, habilidades, realizacoes, tom):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""Você é um especialista em escrita persuasiva e criação de recomendações profissionais personalizadas no LinkedIn. Com base nas informações fornecidas, elabore uma recomendação que destaque as habilidades, realizações e qualidades da pessoa, adaptada ao estilo e tom apropriados para a rede profissional. Certifique-se de:
                    1. Incluir uma breve introdução explicando como você conhece a pessoa e seu contexto profissional.
                    2. Destacar de 2 a 3 habilidades ou competências-chave com exemplos relevantes.
                    3. Enfatizar a contribuição ou impacto que essa pessoa teve no ambiente de trabalho, projetos ou colaboração.
                    4. Finalizar com uma forte recomendação que reforce a confiabilidade e o valor da pessoa no mercado.
                    5. A recomendação deve ser feita em inglês.

                    Gere um texto fluido, natural e persuasivo, com um limite de até 300 palavras.
                """,
            },
            {
                "role": "user",
                "content": f"""
                    **Informações Fornecidas:**
                    - Nome da pessoa: {nome}
                    - Relação profissional: {relacao_profissional}
                    - Habilidades principais: {habilidades}
                    - Realizações notáveis: {realizacoes}
                    - Tom desejado: {tom}
                """,
            }
        ],
        model="gemma2-9b-it",
    )

    return chat_completion.choices[0].message.content

# Interface do Streamlits
st.set_page_config(page_title="Gerador de Recomendações do LinkedIn", page_icon=":robot:")

st.title("🤖 PDSAcademy - Gerador de Recomendações do LinkedIn")
st.write("Este aplicativo gera recomendações profissionais personalizadas para o LinkedIn com base nas informações fornecidas.")
st.write("O objetivo é destacar as habilidades, realizações e qualidades da pessoa, adaptando o estilo e tom apropriados para a rede profissional. 🚀")

# Inputs do usuário
nome = st.text_input("Nome da pessoa:")
relacao_profissional = st.selectbox("Relação profissional:", ["Colega de Trabalho", "Supervisor", "Cliente", "Parceiro", "Outro"])
habilidades = st.text_area("Principais habilidades (separe por vírgulas):")
realizacoes = st.text_area("Realizações notáveis:")
tom = st.selectbox("Tom desejado:", ["Formal", "Informal", "Inspirador"])

gerar = st.button("Gerar Recomendação")

if gerar:
    if nome and relacao_profissional and habilidades and realizacoes:
        try:
            recommendation = generate_recommendation(nome, relacao_profissional, habilidades, realizacoes, tom)
            st.subheader("Recomendação Gerada:")
            st.write(recommendation)
            st.write(f"Tamanho da Recomendação: {len(recommendation)}")
        except Exception as e:
            st.error(f"Erro ao gerar a recomendação: {e}")
    else:
        st.warning("Por favor, preencha todas as informações para gerar a recomendação.")
