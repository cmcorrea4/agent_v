import streamlit as st

def load_elevenlabs_widget():
    # Configurar la página para permitir elementos HTML no seguros
    st.set_page_config(
        page_title="ElevenLabs Chat Widget",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS para asegurar que el widget sea visible
    st.markdown("""
        <style>
            iframe {
                border: none !important;
                min-height: 600px !important;
            }
            .stApp {
                margin: 0;
                padding: 0;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML del widget con estilos adicionales
    elevenlabs_html = """
        <div style="width: 100%; min-height: 600px; margin: 0; padding: 0;">
            <elevenlabs-convai 
                agent-id="gMh8bGtmxS5OxxPwDuKT" 
                style="width: 100%; height: 100%; min-height: 600px;">
            </elevenlabs-convai>
            <script defer src="https://elevenlabs.io/convai-widget/index.js" type="text/javascript"></script>
        </div>
    """
    
    # Renderizar el widget con altura suficiente
    st.components.v1.html(
        elevenlabs_html,
        height=1200,  # Aumentamos la altura
        scrolling=True  # Permitimos scroll si es necesario
    )

def main():
    # Removemos el título para dar más espacio al widget
    load_elevenlabs_widget()

if __name__ == "__main__":
    main()
