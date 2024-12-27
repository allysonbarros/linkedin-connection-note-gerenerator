import os
import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

# Initialize the Groq pipeline
def generate_message(my_experiences, recruiter_name, job_description):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""Você é um assistente responsável por gerar mensagens curtas de conexão no LinkedIn para recrutadores que estão em busca de um talentoso profissional de TI. 
                O objetivo é chamar a atenção do recrutador e despertar o interesse dele em mim como candidato. 
                IMPORTANTE: Você deve retornar APENAS a mensagem. A mensagem deve ser personalizada e direcionada ao recrutador, e não ao candidato. 
                IMPORTANTE: A mensagem deve ser em inglês e ter no máximo 200 caracteres.

                Esse é o meu resumo profissional: {my_experiences}
                """,
            },
            {
                "role": "user",
                "content": f"Escreva uma mensagem em inglês de conexão com obrigatoriamente até 200 carecteres para o recrutador {recruiter_name} sobre a vaga com a seguinte descrição: {job_description}",
            }
        ],
        model="gemma2-9b-it",
    )

    return chat_completion.choices[0].message.content

st.set_page_config(page_title="Gerador de Mensagem de Conexão no LinkedIn", page_icon=":robot:")
st.title("🤖 PDSAcademy - Gerador de Mensagem de Conexão no LinkedIn")
st.write("Este aplicativo gera mensagens curtas de conexão no LinkedIn para recrutadores que estão em busca de profissionais de TI.")
st.write("O objetivo é chamar a atenção do recrutador e despertar o interesse dele em você como candidato. 🚀")

st.subheader("Insira os detalhes da vaga e do recrutador")

my_experiences = st.text_area("Resumo Profissional", height=200)

st.subheader("Insira os detalhes da vaga e do recrutador")

recruiter_name = st.text_input("Nome do Recrutador")
job_description = st.text_area("Descrição da Vaga", height=200)

if st.button("Gerar Mensagem"):
    if my_experiences and recruiter_name and job_description:
        message = generate_message(my_experiences, recruiter_name, job_description)

        # Display the generated message and the size of the message
        st.text_area("Mensagem Gerada", value=message, height=200)
        st.write(f"Tamanho da Mensagem: {len(message)}")
    else:
        st.error("Por favor, preencha todos os campos.")