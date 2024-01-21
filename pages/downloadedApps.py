import streamlit as st
from streamlit import session_state

# Sample data for app cards (replace this with your actual data)
app_data = [
    {"name": "App 1", "image_url": "images/AppCentral logo.png"},
    {"name": "App 2", "image_url": "images/AppCentral logo.png"},
    {"name": "App 3", "image_url": "images/AppCentral logo.png"},
    # Add more app data as needed
]

def delete_app(app_name, session_state):
    # Implement the delete functionality here
    app_data = session_state.app_data
    session_state.app_data = [app for app in app_data if app["name"] != app_name]
    st.warning(f"Click again with you really want to delete {app_name}")

def app_screen(session_state):
    st.title("Apps Instalados")
    
    for app in session_state.app_data:
        # Display app card with name, image, and delete button
        col1, col2, col3 = st.columns([2, 5, 1])
        
        # App name
        col1.subheader(app["name"])
        
        # App image
        col2.image(app["image_url"], use_column_width=True)
        
        # Button to trigger deletion with a unique key based on app name
        delete_button_key = f"delete_button_{app['name']}"
        if col3.button("Delete", key=delete_button_key):
            delete_app(app["name"], session_state)

if __name__ == "__main__":
    if "app_data" not in st.session_state:
        st.session_state.app_data = app_data
    
    app_screen(st.session_state)
