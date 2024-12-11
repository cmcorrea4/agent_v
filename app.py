import streamlit as st

def load_elevenlabs_widget(agent_id="gMh8bGtmxS5OxxPwDuKT", height=500, container_height=600):
    # HTML del widget con el script necesario
    elevenlabs_html = f"""
    <div style="width: 100%; height: {height}px;">
        <elevenlabs-convai agent-id="{agent_id}"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    </div>
    """
    
    # Usar components.html para renderizar el widget
    st.components.v1.html(elevenlabs_html, height=container_height)

def main():
    st.title("Mi Aplicación con ElevenLabs Widget")
    
    # Configuraciones del widget
    with st.sidebar:
        st.header("Configuración del Widget")
        widget_height = st.slider("Altura del Widget", 300, 800, 500)
        container_height = st.slider("Altura del Contenedor", 400, 900, 600)
