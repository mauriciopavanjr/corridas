from bs4 import BeautifulSoup
import pandas as pd

class BuscaElementos:
    def __init__(self, response):
        self.response = response

    def busca_elementos(self):
        """
        Função que busca os dados no response da url 
        Parametro: 
            response(classe response do requests): response da url
            informada na inicialização da classe
        Retorno:  
            dados (Data Frame): dataframe com os dados coletados no site
        """
        try:
            dados = []
            soup = BeautifulSoup(self.response.text, 'html.parser')
            table_elements = soup.find_all('table', class_='table table-striped')[0]
            tr_elements = table_elements.find_all('tr')
            for tr in tr_elements:
                td_elements = tr.find_all('td')
                if td_elements:
                    dados.append({
                        'Prova': td_elements[0].get_text(),
                        'Local': td_elements[1].get_text(),
                        'Distância': td_elements[2].get_text(),
                        'Data': td_elements[3].get_text(),
                        'Link': td_elements[4].find('a')['href']
                    })

            df = pd.DataFrame(dados)
            return df
        except:
            return None