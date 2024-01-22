import streamlit as st
import uuid
from streamlit_extras.switch_page_button import switch_page


def create_card(title, category, image_url):
    st.markdown("""
        <style>
        div.stColumn {
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 8])
    with col1:
        st.image(image_url, use_column_width='auto', caption=category)
    with col2:
        st.write(f"# {title}")
        st.write(f"**Categoria:** {category}")
        if st.button(f"Baixar {title}"):
            switch_page("downloadedApps")

def generate_unique_key():
    return str(uuid.uuid4())

def recommend():
    apps = [
        {"nome": "TikTok", "categoria": "Entretenimento", "imagem_url": "https://via.placeholder.com/150"},
        {"nome": "MyMQTT", "categoria": "Tecnologia", "imagem_url": "https://via.placeholder.com/150"},
        {"nome": "HayDay", "categoria": "Jogo", "imagem_url": "https://via.placeholder.com/150"},
        {"nome": "Pinterest", "categoria": "Arte", "imagem_url": "https://via.placeholder.com/150"},
        {"nome": "Amazon", "categoria": "Comércio", "imagem_url": "https://via.placeholder.com/150"}
    ]
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
    col1, col2 = st.columns([4, 1])  # Divide a tela em 4/5 para o texto e 1/5 para a imagem
    col1.title("Olá Lidia!")
    col1.header("Divirta-se com nossos apps!")

    recommendations = recommend()

    for recommendation in recommendations:
        create_card(recommendation["nome"], recommendation["categoria"], recommendation["imagem_url"])

    # Botão para atualizar a página
    st.button("Mostrar outros apps")

# Função principal do aplicativo Streamlit
def main():
    recommend_app()

if __name__ == "__main__":
    main()
