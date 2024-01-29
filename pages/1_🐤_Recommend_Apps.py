import random
import streamlit as st
from services.app_service import RequestSender

def create_card(title, category, type, price, content_rat, genre, session_state, key):
    st.markdown("""
        <style>
        div.stColumn {
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("https://cdn.dribbble.com/users/1726280/screenshots/18021506/media/ff2e1b1ee03ca15f6d7c96bbaad19be5.jpg", use_column_width='auto')
    with col2:
        st.write(f"<h1 style='font-size: 24px;'>{title}</h1>", unsafe_allow_html=True)
        if st.button("Download", key=f"{title}--{key}"):
            # Add the clicked app to the session state if it's not already there with status 1
            app_data = session_state.get("app_data", {})
            if title not in app_data or app_data[title]["status"] != 1:
                app_data[title] = {"category": category, "type": type, "price": price, "content_rating": content_rat, "genres": genre, "status": 1}
                session_state.app_data = app_data
                st.experimental_rerun()

def display_other_apps(session_state):
    app_data = session_state.get("app_data", {})
    status_1_count = sum(1 for app_info in app_data.values() if app_info.get("status") == 1)
    status_0_count = sum(1 for app_info in app_data.values() if app_info.get("status") == 0)

    if status_1_count >= 2 and status_0_count >= 2:
        st.button("Display Other Apps", on_click=lambda: display_recommendations_by_download(session_state))

def display_recommendations_by_download(session_state):
    request_sender = RequestSender("http://127.0.0.1:5000")
    recommendations = request_sender.send_recommendations_by_download(session_state.app_data)
    
    if recommendations:
        st.header("Additional Recommendations")

        # Shuffle the recommendations list to get random order
        recommendations_list = recommendations.get("recommendations", [])
        random.shuffle(recommendations_list)

        # Display up to 10 randomly selected recommendations
        if len(recommendations_list) >= 10:
            for index, recommendation in enumerate(recommendations_list[:10]):
                create_card(recommendation["App"], recommendation["Category"], recommendation["Type"], recommendation["Price"], recommendation["Content Rating"], 
                            recommendation["Genres"], session_state, index)
        else:
            st.write("Not enough recommendations available yet.")

def recommend_app(session_state):
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

    name = session_state.get("user_name", "Guest")
    col1, _ = st.columns([4, 1]) 
    col1.title(f"Olá {name}!")
    col1.header("Divirta-se com nossos apps!")

    recommendations = session_state.get("recommendations", [])
    for index, recommendation in enumerate(recommendations):
        app_title = recommendation["App"]
        app_data = session_state.get("app_data", {})
        if app_title not in app_data or app_data[app_title]["status"] != 1:
            create_card(app_title, recommendation["Category"], recommendation["Type"], recommendation["Price"], recommendation["Content Rating"], 
                        recommendation["Genres"], session_state, index)

    display_other_apps(session_state)

def main():
    recommend_app(st.session_state)

if __name__ == "__main__":
    main()