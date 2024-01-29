import streamlit as st

def update_app_status(app_name, session_state):
    # Update the status of the app to 0
    app_data = session_state.app_data
    if app_name in app_data:
        app_data[app_name]["status"] = 0
        session_state.app_data = app_data
        st.warning(f"Press delete again to confirm")
    else:
        st.error(f"App '{app_name}' not found in app data.")

def app_screen(session_state):
    st.title("Apps Instalados")

    print(session_state.app_data)
    
    if "app_data" not in session_state:
        session_state.app_data = {}

    # Filter out apps with status 0
    active_apps = {app_name: app_info for app_name, app_info in session_state.app_data.items() if app_info["status"] == 1}

    for app_name, app_info in active_apps.items():
        # Display app card with name, image, and update button
        col1, col2, col3 = st.columns([2, 5, 1])
        
        # App name
        col1.subheader(app_name)
        
        # App image
        col2.image("https://cdn.dribbble.com/users/1726280/screenshots/18021506/media/ff2e1b1ee03ca15f6d7c96bbaad19be5.jpg", use_column_width=True)
        
        # Button to update status with a unique key based on app name
        update_button_key = f"update_button_{app_name}"
        if col3.button("Delete", key=update_button_key):
            update_app_status(app_name, session_state)

if __name__ == "__main__":
    app_screen(st.session_state)
