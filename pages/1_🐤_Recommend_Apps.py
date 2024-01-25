import streamlit as st
import uuid
from streamlit_extras.switch_page_button import switch_page


def create_card(title, category):
    st.markdown("""
        <style>
        div.stColumn {
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("https://cdn.dribbble.com/users/1726280/screenshots/18021506/media/ff2e1b1ee03ca15f6d7c96bbaad19be5.jpg", use_column_width='auto', caption=category)
    with col2:
        st.write(f"<h1 style='font-size: 24px;'>{title}</h1>", unsafe_allow_html=True)
        st.write(f"**Categoria:** {category}")


def generate_unique_key():
    return str(uuid.uuid4())

def recommend():
    apps = []
    return apps

# Função para criar o aplicativo Streamlit
def recommend_app():
    st.markdown(
        """
        <style>
        body {
            background-color: #3498db;
            color: #fff;  /* Define a cor do texto como branco */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Adicionando imagem à direita do título
    name = st.session_state.get("user_name")
    col1, col2 = st.columns([4, 1]) 
    col1.title(f"Olá {name}!")
    col1.header("Divirta-se com nossos apps!")

    recommendations = st.session_state.get("recommendations", []) 
    for recommendation in recommendations[:3]:
        create_card(recommendation["App"], recommendation["Category"])

    # Botão para atualizar a página
    st.button("Mostrar outros apps")

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()
