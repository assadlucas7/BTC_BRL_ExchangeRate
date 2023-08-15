# Realtime Bitcoin to BRL Exchange Rate Monitor

## Descrição

Este projeto fornece uma interface gráfica simples para verificar a taxa de câmbio em tempo real entre Bitcoin e BRL (Real Brasileiro). Ele utiliza a API da Alphavantage para obter os dados.

## Pré-requisitos

- Você precisará de uma chave de API da Alphavantage para usar este programa.

## Como Usar

1. **Obtendo a chave de API**:
   - Acesse [Alphavantage](https://www.alphavantage.co/support/#api-key) e registre-se para obter sua chave de API gratuita.
    
2. **Configurando o Programa**:
   - Após obter sua chave, localize a seguinte linha no código:
     ```python
     url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=BRL&apikey=YOUR_API_KEY'
     ```
     Substitua `YOUR_API_KEY` pela chave de API que você recebeu.

3. **Instale as dependências necessárias**:
   ```bash
   pip install requests tk

4. **Execute o programa**:
   - Use o comando abaixo no seu terminal ou prompt de comando:
     ```bash
     python nome_do_seu_arquivo.py
     ```
   - Após iniciar o programa, uma interface gráfica será exibida.
   - Clique no botão "Buscar Taxa de Câmbio" para obter a taxa de câmbio atual.

## Recursos

- Interface gráfica simples e amigável.
- Taxas de câmbio em tempo real fornecidas pela API da Alphavantage.

## Contribuição

Se deseja contribuir para este projeto, sinta-se à vontade para abrir um Pull Request ou Issue no GitHub.

## Licença

MIT License
