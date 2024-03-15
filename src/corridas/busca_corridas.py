import requests
from datetime import datetime, timedelta

class BuscaCorridas:
    def __init__(self, api_url):
        self.api_url = api_url

    def buscar_corridas(self):
        """
        Função que realiza a requisição na url 
        Parametro: 
            api_url(string): string com a url a ser realizada a requisicao
            informada na inicialização da classe
        Retorno:  
            resposta (classe response do requests): response da url fornecida 
        """
        try:
            resposta = requests.get(self.api_url)
            resposta.raise_for_status()
            return resposta
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar corridas: {e}")
            return None


