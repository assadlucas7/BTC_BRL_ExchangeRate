import requests
from tkinter import *

# Função para buscar a taxa de câmbio
def get_exchange_rate():
    # Limpar a área de texto
    text_area.delete(1.0, END)
    
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=BRL&apikey=YOUR_API_KEY'
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()
        visual_data = data.get('Realtime Currency Exchange Rate', None)
        
        if visual_data:
            # Atualizando a interface com os dados
            for key, value in visual_data.items():
                text_area.insert(END, f"{key} : {value}\n")
        else:
            text_area.insert(END, "Erro ao obter os dados desejados.\n")
    else:
        text_area.insert(END, "Erro ao buscar dados.\n")

# Inicializando a interface Tkinter
root = Tk()
root.title("Bitcoin-BRL Exchange Rate")

# Adicionando botão para buscar a taxa de câmbio
fetch_button = Button(root, text="Buscar Taxa de Câmbio", command=get_exchange_rate)
fetch_button.pack(pady=20)

# Área de texto para mostrar os resultados
text_area = Text(root, height=10, width=50)
text_area.pack(pady=20)
text_area.insert(END, "Pressione o botão acima para buscar a taxa de câmbio.\n")

# Rodando a interface
root.mainloop()

