# Procurador de carta de Magic - Londrina


## Descrição:

O objetivo do programa é melhorar a velocidade de pesquisa de cartas de Magic em lojas no [MYP](https://mypcards.com/magic), inicialmente o programa funciona com os 3 maiores de Londrina: [Piedade](https://mypcards.com/Piedade), [Wlad](https://mypcards.com/Wlad) e [basdao](https://mypcards.com/basdao).

## Como funciona:
*****************************
Ao rodar o programa, é necessário inserir o nome da carta desejada para pesquisa, em seguida o script verifica se a carta existe no banco de dados do Scryfall e returna a carta com a melhor conpatibiidade, caso não exista, o programa vai dar um reprompt. Com o web scrapping do *_BeautifulSoup_* é póssivel extrair informaçoes da carta desejada em cada uma das lojas, retornando em forma tabulada os dados obtidos.

## Pip:

É possível usar o pip com esse programa, da seguinte forma:
```python 
pip install magiclondrina
```
```python 
import magic.londrina as magic

magic.get_info("Nome da carta")
```
