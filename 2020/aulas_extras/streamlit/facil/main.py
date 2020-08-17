from pages.micro_report import MicroReport
import streamlit as st



def load_pages():
    """Carregando paginas que serão exibidas

    Returns:
        dict: {Nome da pagina: Pagina}
    """

    pages = dict()
    
    pages['Netflix'] = MicroReport('relatorio')

    return pages


def main():

    """Corpo e roteamento da página
    """

    pages = load_pages()

    st.header('Tutorial Streamlit')

    st.sidebar.markdown("# Navegação")

    goto = st.sidebar.radio("Ir para", list(pages.keys()))

    pages[goto].render()


if __name__ == "__main__":
	main()

