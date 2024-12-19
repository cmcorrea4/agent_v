import streamlit as st

def load_elevenlabs_widget():
    # Configuración inicial de la página
    st.set_page_config(
        page_title="GETME - Servicios Premium",
        layout="centered",  # Cambiamos a centered para mejor control
        initial_sidebar_state="collapsed"
    )
    
    # Aplicamos estilos CSS directamente
    st.markdown("""
        <style>
            /* Reset de estilos base */
            .stApp {
                background-color: #1E1E1E !important;
            }
            
            /* Ocultar elementos de Streamlit que no necesitamos */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Estilos para el contenedor principal */
            .get-me-container {
                background-color: #2D2D2D;
                border-radius: 20px;
                padding: 20px;
                margin: 50px auto;
                max-width: 800px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            /* Estilos para el título */
            .get-me-title {
                color: #FFD700;
                font-family: 'Arial', sans-serif;
                font-size: 36px;
                text-align: center;
                margin-bottom: 20px;
                font-weight: bold;
            }
            
            /* Estilos para el widget de ElevenLabs */
            iframe {
                border: none !important;
                border-radius: 10px !important;
                background: #333333 !important;
                margin: 0 auto !important;
                display: block !important;
                min-height: 600px !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Estructura HTML con los elementos centrados
    st.markdown("""
        <div class="get-me-container">
            <h1 class="get-me-title">GETME</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Widget de ElevenLabs
    elevenlabs_html = """
        <div style="width: 100%; min-height: 600px; margin: 20px auto;">
            <elevenlabs-convai 
                agent-id="gMh8bGtmxS5OxxPwDuKT" 
                style="width: 100%; height: 600px; border-radius: 10px;">
            </elevenlabs-convai>
            <script defer src="https://elevenlabs.io/convai-widget/index.js" type="text/javascript"></script>
        </div>
    """
    
    # Renderizamos el widget
    st.components.v1.html(
        elevenlabs_html,
        height=650,  # Altura fija para evitar problemas de scroll
        scrolling=False
    )

if __name__ == "__main__":
    load_elevenlabs_widget()
