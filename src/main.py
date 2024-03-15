from corridas.busca_corridas import BuscaCorridas
from utils.busca_elementos import BuscaElementos
from utils.show_dados import ShowDados

if __name__ == '__main__':
    url = 'https://www.eucorro.com/calendario/'
    busca_corrida = BuscaCorridas(url)
    corridas_text = busca_corrida.buscar_corridas()
    if corridas_text:
        busca_elementos = BuscaElementos(corridas_text)
        df_corridas = busca_elementos.busca_elementos()
        if not df_corridas.empty:
            show_dados = ShowDados(df_corridas)
            show_dados.imprimir_corridas()