import streamlit as st

def setup_styling():
    # Estilos personalizados para una apariencia premium
    st.markdown("""
        <style>
            /* Estilos generales para toda la aplicación */
            .stApp {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                color: #ffffff;
                font-family: 'Helvetica Neue', sans-serif;
            }
            
            /* Contenedor principal centrado */
            .main-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }
            
            /* Estilos para el widget */
            .widget-container {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                padding: 2rem;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                width: 100%;
                max-width: 800px;
                margin: 2rem auto;
            }
            
            /* Estilos para el logo y título */
            .brand {
                text-align: center;
                margin-bottom: 2rem;
            }
            
            .brand h1 {
                color: #gold;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: 2px;
                margin: 0;
            }
            
            .brand p {
                color: #cccccc;
                font-size: 1.1rem;
                margin-top: 0.5rem;
            }
            
            iframe {
                border: none !important;
                min-height: 600px !important;
                border-radius: 15px;
                background: rgba(255, 255, 255, 0.02);
            }
        </style>
    """, unsafe_allow_html=True)

def load_elevenlabs_widget():
    st.set_page_config(
        page_title="GETME - Asistente de Servicios Premium",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    setup_styling()
    
    # Estructura HTML con diseño mejorado
    premium_html = """
        <div class="main-container">
            <div class="brand">
                <h1>GETME</h1>
                <p>Su asistente personal de servicios premium</p>
            </div>
            <div class="widget-container">
                <elevenlabs-convai 
                    agent-id="gMh8bGtmxS5OxxPwDuKT" 
                    style="width: 100%; height: 100%; min-height: 600px;">
                </elevenlabs-convai>
                <script defer src="https://elevenlabs.io/convai-widget/index.js" type="text/javascript"></script>
            </div>
        </div>
    """
    
    st.components.v1.html(
        premium_html,
        height=1000,
        scrolling=False
    )

def main():
    load_elevenlabs_widget()

if __name__ == "__main__":
    main()
