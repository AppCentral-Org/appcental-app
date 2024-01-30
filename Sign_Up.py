import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from services.app_service import RequestSender

# Dicionário de associação entre categorias e gêneros
categories_to_genres = {'Arte e Design': ['Arte e Design', 'Arte e Design - Pretend Play', 'Arte e Design - Ação e Aventura'], 
                        'Auto e Veículos': ['Auto e Veículos'], 
                        'Livros e Referências': ['Livros e Referências'], 
                        'Negócios': ['Negócios'], 
                        'Quadrinhos': ['Quadrinhos', 'Quadrinhos - Criatividade'], 
                        'Comunicação': ['Comunicação', 'Comunicação - Criatividade'], 
                        'Educação': ['Educação - Educação', 'Educação', 'Educação - Pretend Play'], 
                        'Entretenimento': ['Entretenimento', 'Entretenimento - Música e Vídeo', 
                                           'Entretenimento - Educação'], 
                        'Eventos': ['Eventos'], 
                        'Finanças': ['Finanças'], 
                        'Comida e Bebida': ['Comida e Bebida'], 
                        'Saúde e Fitness': ['Saúde e Fitness', 
                                            'Saúde e Fitness - Ação e Aventura', 'Saúde e Fitness - Educação'], 
                        'Casa e Família': ['Casa e Família'], 
                        'Bibliotecas e Demonstração': ['Bibliotecas e Demonstração'], 
                        'Estilo de Vida': ['Estilo de Vida', 'Estilo de Vida - Pretend Play', 'Estilo de Vida - Educação'], 
                        'Médicos': ['Médico'], 
                        'Social': ['Social'], 
                        'Compras': ['Compras'], 
                        'Fotografia': ['Fotografia'], 
                        'Esportes': ['Esportes'], 
                        'Viagem e Local': ['Viagem e Local', 'Viagem e Local - Ação e Aventura'], 
                        'Ferramentas': ['Ferramentas', 'Ferramentas - Educação'], 
                        'Personalização': ['Personalização'], 
                        'Produtividade': ['Produtividade'], 
                        'Paternidade': ['Paternidade', 'Paternidade - Jogos Cerebrais'], 
                        'Clima': ['Clima'], 
                        'Notícias e Revistas': ['Notícias e Revistas'], 
                        'Mapas e Navegação': ['Mapas e Navegação']}

category_mapping = {'FAMILY': 0.0, 
                    'GAME': 0.03, 
                    'TOOLS': 0.06, 
                    'BUSINESS': 0.1, 
                    'MEDICAL': 0.13, 
                    'PRODUCTIVITY': 0.16, 
                    'PERSONALIZATION': 0.19, 
                    'LIFESTYLE': 0.23, 
                    'FINANCE': 0.26, 
                    'SPORTS': 0.29, 
                    'COMMUNICATION': 0.32, 
                    'HEALTH_AND_FITNESS': 0.35, 
                    'PHOTOGRAPHY': 0.39, 
                    'NEWS_AND_MAGAZINES': 0.42, 
                    'BOOKS_AND_REFERENCE': 0.45, 
                    'TRAVEL_AND_LOCAL': 0.48, 
                    'SHOPPING': 0.52, 
                    'SOCIAL': 0.55, 
                    'VIDEO_PLAYERS': 0.58, 
                    'MAPS_AND_NAVIGATION': 0.61, 
                    'EDUCATION': 0.65, 
                    'FOOD_AND_DRINK': 0.68, 
                    'ENTERTAINMENT': 0.71, 
                    'AUTO_AND_VEHICLES': 0.74, 
                    'LIBRARIES_AND_DEMO': 0.77, 
                    'WEATHER': 0.81, 
                    'HOUSE_AND_HOME': 0.84, 
                    'EVENTS': 0.87, 'ART_AND_DESIGN': 0.9, 'PARENTING': 0.94, 'BEAUTY': 0.97, 'COMICS': 1.0}


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
        max_price = 0

    # Select box for content rating
    content_ratings = ['Todos', 'Adolescentes', 'Todos 10+', 'Não Classificado']
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
        user_name = {
            'user_name': name
        }
        print(app_serv.send_user_name(user_name))
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
