class ShowDados():
    def __init__(self, df_corridas):
        self.df_corridas = df_corridas
    
    def imprimir_corridas(self):
        """
        Função que imprime os dados no response da url 
        Parametro: 
            df_corridas(dataframe): dataframe com os dados das corridas
            informada na inicialização da classe
        """
        for index, corrida in self.df_corridas.iterrows():
            print(f"Prova: {corrida['Prova']}")
            print(f"Local: {corrida['Local']}")
            print(f"Distância: {corrida['Distância']}")
            print(f"Data: {corrida['Data']}")
            print(f"Link: {corrida['Link']}")
            print("="*30)
