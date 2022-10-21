from bs4 import BeautifulSoup
import requests as re
from tabulate import tabulate
import scrython
import os
import time


def main():
    while True:
        card_name = input("Nome da carta:  ")
        print("Pesquisando carta na base de dados...")
        card_name = get_card(card_name)
        time.sleep(1)
        os.system('cls')
        if card_name is None:
            continue
        url, url_wlad, url_basdao = get_url(card_name)
        card_info = get_info(url, url_wlad, url_basdao)
        get_tables(card_info)
        reprompt = input("Pesquisar outra carta [s/n] ? ")
        while reprompt != "s" and reprompt != "n":
            reprompt = input("Digite [s] para SIM ou [n] para NÃO: ")
        if reprompt == "s":
            pass
        else:
            break


def get_url(card_name):
    url = "https://mypcards.com/Piedade/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch" \
               "%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=" + f"{card_name.replace(' ', '+').strip()}" + "&" \
               "PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D=20"

    url_wlad = "https://mypcards.com/Wlad/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch" \
               "%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=" + f"{card_name.replace(' ', '+').strip()}" + "&" \
               "PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D=20"

    url_basdao = "https://mypcards.com/basdao/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch" \
                 "%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=" + f"{card_name.replace(' ', '+').strip()}" + "&" \
                 "PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D=20"

    return url, url_wlad, url_basdao


def get_info(*args):
    card_dict = dict()
    card_list = dict()
    info = ""
    n = 0

    for arg in args:
        card_dict.clear()
        number = 1

        if n == 0:
            loja = "w1"
            nome_loja = "Piedade"
            n = n + 1
        elif n == 1:
            loja = "w0"
            nome_loja = "Wlad"
            n = n + 1
        else:
            loja = "w0"
            nome_loja = "basdao"

        response = re.get(arg).text
        soup = BeautifulSoup(response, "lxml")
        tags = soup.find_all("div", id=loja, class_="row")
        cards = tags[0].find("ul", class_="stream-list")

        try:
            for card in cards:
                items = str(card.text).strip()
                items = items.replace("Comprar", "").replace("Foil", "").replace("un ", "").replace("\xa0", "")

                for lines in items.splitlines():
                    lines = lines.strip()
                    if lines.startswith("R$") is True:
                        info = info + lines
                        card_dict[number] = info
                        number = number + 1
                        info = ""
                        continue
                    if lines == "":
                        continue
                    info = info + lines + "@"
                    card_dict[number] = info
            card_list.update({nome_loja: card_dict.copy()})
        except TypeError:
            card_dict[1] = "Nenhum resultado encontrado"
            card_list[nome_loja] = card_dict.copy()
            continue
    return card_list


def get_tables(card_info):
    n = 0
    try:
        if card_info["Piedade"][1] == "Nenhum resultado encontrado":
            headers = ["Piedade"]
            values = [["Nenhum resultado encontrado"]]
            print(tabulate(values, headers=headers, tablefmt="grid"))
        else:
            headers = ["Piedade", "Nome PT", "Nome ING", "Coleção", "Qualidade", "Quantidade", "Preço"]
            values = [[key, *value.split("@")] for key, value in card_info["Piedade"].items()]
            print(tabulate(values, headers=headers, tablefmt="grid"))
    except KeyError:
        n = n + 1
        pass
    try:
        if card_info["Wlad"][1] == "Nenhum resultado encontrado":
            headers = ["Wlad"]
            values = [["Nenhum resultado encontrado"]]
            print(tabulate(values, headers=headers, tablefmt="grid"))
        else:
            headers = ["Wlad", "Nome PT", "Nome ING", "Coleção", "Qualidade", "Quantidade", "Preço"]
            values = [[key, *value.split("@")] for key, value in card_info["Wlad"].items()]
            print(tabulate(values, headers=headers, tablefmt="grid"))
    except KeyError:
        n = n + 1
        pass
    try:
        if card_info["basdao"][1] == "Nenhum resultado encontrado":
            headers = ["basdao"]
            values = [["Nenhum resultado encontrado"]]
            print(tabulate(values, headers=headers, tablefmt="grid"))
        else:
            headers = ["basdao", "Nome PT", "Nome ING", "Coleção", "Qualidade", "Quantidade", "Preço"]
            values = [[key, *value.split("@")] for key, value in card_info["basdao"].items()]
            print(tabulate(values, headers=headers, tablefmt="grid"))
    except KeyError:
        n = n + 1
        pass
    return n


def get_card(card_name):
    try:
        card = scrython.cards.Named(fuzzy=card_name)
        card_name = str(card.name())
    except scrython.foundation.ScryfallError:
        print("Carta não encontrada. ")
        return None
    return card_name


if __name__ == "__main__":
    main()
