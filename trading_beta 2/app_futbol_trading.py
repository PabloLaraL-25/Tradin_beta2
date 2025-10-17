import streamlit as st
import importlib.util
import os

def main():
    st.set_page_config(page_title="Fútbol y Trading", layout="wide")
    st.title("Análisis Deportivo y Trading")
    pagina = st.sidebar.selectbox('Selecciona la página', ['Fútbol', 'Trading'])

    # Verificar que los archivos existen en el mismo directorio
    base_dir = os.path.dirname(__file__)
    futbol_path = os.path.join(base_dir, 'app_futbol.py')
    trading_path = os.path.join(base_dir, 'trading_beta1.py')

    if pagina == 'Fútbol':
        if not os.path.exists(futbol_path):
            st.error('No se encontró app_futbol.py en el mismo directorio. Sube todos los archivos juntos.')
            st.stop()
        spec = importlib.util.spec_from_file_location('app_futbol', 'app_futbol.py')
        app_futbol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_futbol)
        app_futbol.mostrar_app_futbol()
        st.stop()
    elif pagina == 'Trading':
        if not os.path.exists(trading_path):
            st.error('No se encontró trading_beta1.py en el mismo directorio. Sube todos los archivos juntos.')
            st.stop()
        spec = importlib.util.spec_from_file_location('trading_beta1', 'trading_beta1.py')
        trading_beta1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(trading_beta1)
        if hasattr(trading_beta1, 'mostrar_app_trading'):
            trading_beta1.mostrar_app_trading()
        else:
            st.info('La función de trading se encuentra en trading_beta1.py. Si quieres una interfaz visual, agrega una función mostrar_app_trading() en ese archivo.')

if __name__ == "__main__":
    main()
