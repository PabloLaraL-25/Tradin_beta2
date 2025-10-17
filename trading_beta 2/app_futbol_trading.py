import streamlit as st
import importlib.util

def main():
    st.set_page_config(page_title="Fútbol y Trading", layout="wide")
    st.title("Análisis Deportivo y Trading")
    pagina = st.sidebar.selectbox('Selecciona la página', ['Fútbol', 'Trading'])

    if pagina == 'Fútbol':
        # Importar y ejecutar la app de fútbol
        spec = importlib.util.spec_from_file_location('app_futbol', 'app_futbol.py')
        app_futbol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_futbol)
        app_futbol.mostrar_app_futbol()
        st.stop()
    elif pagina == 'Trading':
        # Importar y ejecutar la app de trading (solo la lógica de trading)
        spec = importlib.util.spec_from_file_location('trading_beta1', 'trading_beta1.py')
        trading_beta1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(trading_beta1)
        if hasattr(trading_beta1, 'mostrar_app_trading'):
            trading_beta1.mostrar_app_trading()
        else:
            st.info('La función de trading se encuentra en trading_beta1.py. Si quieres una interfaz visual, agrega una función mostrar_app_trading() en ese archivo.')

if __name__ == "__main__":
    main()
