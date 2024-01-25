import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from services.app_service import RequestSender

# Dicionário de associação entre categorias e gêneros
categories_to_genres = {
    'Arte e Design': ['Arte e Design', 'Arte e Design - Pretend Play', 'Arte e Design - Criatividade', 'Arte e Design - Ação e Aventura'],
    'Auto e Veículos': ['Auto e Veículos'],
    'Beleza': ['Beleza'],
    'Livros e Referências': ['Livros e Referências', 'Livros e Referências - Criatividade', 'Livros e Referências - Educação'],
    'Negócios': ['Negócios'],
    'Quadrinhos': ['Quadrinhos', 'Quadrinhos - Criatividade'],
    'Comunicação': ['Comunicação', 'Comunicação - Criatividade'],
    'Encontros': ['Encontros'],
    'Educação': ['Educação - Educação', 'Educação', 'Educação - Criatividade', 'Educação - Música e Vídeo', 'Educação - Ação e Aventura', 'Educação - Pretend Play', 'Educação - Jogos Cerebrais'],
    'Entretenimento': ['Entretenimento', 'Entretenimento - Música e Vídeo', 'Entretenimento - Jogos Cerebrais', 'Entretenimento - Criatividade', 'Entretenimento - Educação', 'Entretenimento - Pretend Play'],
    'Eventos': ['Eventos'],
    'Finanças': ['Finanças'],
    'Comida e Bebida': ['Comida e Bebida'],
    'Saúde e Fitness': ['Saúde e Fitness', 'Saúde e Fitness - Ação e Aventura', 'Saúde e Fitness - Educação'],
    'Casa e Família': ['Casa e Família'],
    'Bibliotecas e Demonstração': ['Bibliotecas e Demonstração'],
    'Estilo de Vida': ['Estilo de Vida', 'Estilo de Vida - Pretend Play', 'Estilo de Vida - Educação'],
    'Jogos': ['Jogos', 'Jogos - Ação e Aventura', 'Jogos - Educação', 'Jogos Cerebrais'],
    'Família': ['Família'],
    'Médicos': ['Médico'],
    'Social': ['Social'],
    'Compras': ['Compras'],
    'Fotografia': ['Fotografia'],
    'Esportes': ['Esportes', 'Esportes - Ação e Aventura'],
    'Viagem e Local': ['Viagem e Local', 'Viagem e Local - Ação e Aventura'],
    'Ferramentas': ['Ferramentas', 'Ferramentas - Educação'],
    'Personalização': ['Personalização'],
    'Produtividade': ['Produtividade'],
    'Paternidade': ['Paternidade', 'Paternidade - Música e Vídeo', 'Paternidade - Educação', 'Paternidade - Jogos Cerebrais'],
    'Clima': ['Clima'],
    'Reprodutores de Vídeo': ['Reprodutores de Vídeo', 'Reprodutores de Vídeo - Música e Vídeo', 'Reprodutores de Vídeo - Criatividade'],
    'Notícias e Revistas': ['Notícias e Revistas'],
    'Mapas e Navegação': ['Mapas e Navegação'],
}

app_serv = RequestSender('http://127.0.0.1:5000')

st.set_page_config(
    page_title="Sign Up",
    page_icon="👋",
)

def get_genres_for_category(category):
    return categories_to_genres.get(category, [])

def signup():
    # Configurando a cor do fundo para azul
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
    col1.title("Bem-Vindo ao AppCentral")
    col1.header("Cadastre seu nome e preferências")

    # Text input for name
    name = col1.text_input("Nome")

    # Select box for category
    categories = list(categories_to_genres.keys())
    selected_category = col1.selectbox("Categoria", categories)

    # Radio button for type
    types = ['Grátis', 'Pago']
    selected_type = col1.radio("Tipo", types)

    # Display max price slider only if the user chooses the "Paid" option
    if selected_type == 'Pago':
        max_price = col1.slider("Preço Máximo", min_value=0.0, max_value=400.0, value=1.0, step=0.1)
    else:
        max_price = None

    # Select box for content rating
    content_ratings = ['Todos', 'Adolescentes', 'Todos 10+', 'Mature 17+', 'Adultos 18+', 'Não Classificado']
    selected_content_rating = col1.selectbox("Classificação de Conteúdo", content_ratings)

    # Select box for genre based on the selected category
    genres = get_genres_for_category(selected_category)
    if len(genres) > 1:
        selected_genre = col1.selectbox("Gênero", genres)
    else:
        selected_genre = genres[0] if genres else None

    # Button for sign up
    if col1.button("Cadastrar"):
        attributes = {
                'category': selected_category, 
                'type': selected_type,
                'price': max_price,
                'content_rating': selected_content_rating,
                'genres': selected_genre,
            }
        
        print(app_serv.send_request(attributes))
        recommendations = app_serv.send_request(attributes)['recommendations']
        st.session_state.recommendations = recommendations
        st.session_state.user_name = name

        switch_page("Recommend Apps")

        # Armazene as recomendações em session_state
        

        # Perform actions when the button is clicked
        col1.success("Cadastro realizado com sucesso!")
        col1.write(f"Nome: {name}")
        col1.write(f"Categoria: {selected_category}")
        col1.write(f"Tipo: {selected_type}")
        if max_price is not None:
            col1.write(f"Preço Máximo: {max_price}")
        col1.write(f"Classificação de Conteúdo: {selected_content_rating}")
        col1.write(f"Gênero: {selected_genre}")


    # Ajustando a posição e tamanho da imagem
    col2.image("images/AppCentral logo.png", width=300)
    col2.markdown("<br>", unsafe_allow_html=True)  # Adicionando espaço após a imagem

if __name__ == "__main__":
    signup()
