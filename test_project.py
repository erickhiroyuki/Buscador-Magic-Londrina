from project import get_url, get_info, get_tables, get_card


def test_url():
    assert get_url("veto de dovin") == ("https://mypcards.com/Piedade/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                        "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin"
                                        "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                        "=20",
                                        "https://mypcards.com/Wlad/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                        "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin"
                                        "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                        "=20",
                                        "https://mypcards.com/basdao/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                        "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin"
                                        "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                        "=20")
    assert get_url("Mana vault") == ("https://mypcards.com/Piedade/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                     "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=Mana+Vault"
                                     "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                     "=20",
                                     "https://mypcards.com/Wlad/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                     "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=Mana+Vault"
                                     "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                     "=20",
                                     "https://mypcards.com/basdao/magic?PastaSearch%5BexibirSomenteVenda%5D=0"
                                     "&PastaSearch%5BexibirSomenteVenda%5D=1&PastaSearch%5Bquery%5D=Mana+Vault"
                                     "&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch%5BquantidadeRegistro%5D"
                                     "=20")


def test_info():
    url = "https://mypcards.com/Piedade/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch%5BexibirSomenteVenda" \
          "%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch" \
          "%5BquantidadeRegistro%5D=20 "
    url_2 = "https://mypcards.com/Wlad/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch%5BexibirSomenteVenda" \
            "%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch" \
            "%5BquantidadeRegistro%5D=20 "
    url_3 = "https://mypcards.com/basdao/magic?PastaSearch%5BexibirSomenteVenda%5D=0&PastaSearch%5BexibirSomenteVenda" \
            "%5D=1&PastaSearch%5Bquery%5D=veto+de+dovin&PastaSearch%5BexibirSomenteDesejos%5D=0&PastaSearch" \
            "%5BquantidadeRegistro%5D=20 "
    assert get_info(url, url_2, url_3) == ({'Piedade': {1: "Veto de Dovin@Dovin's Veto@PWAR@NM@1 Un.@R$19,00"}, 'Wlad': {1: "Veto de Dovin@Dovin's Veto@WAR@NM@3 Un.@R$11,25", 2: "Veto de Dovin@Dovin's Veto@WAR@NM@1 Un.@R$11,25"}, 'basdao': {1: "Veto de Dovin@Dovin's Veto@WAR@NM@9 Un.@R$9,99"}})


def test_table():
    assert get_tables({'Piedade': {1: "Veto de Dovin@Dovin's Veto@PWAR@NM@1 Un.@R$19,00"}, 'Wlad': {1: "Veto de Dovin@Dovin's Veto@WAR@NM@3 Un.@R$11,25", 2: "Veto de Dovin@Dovin's Veto@WAR@NM@1 Un.@R$11,25"}, 'basdao': {1: "Veto de Dovin@Dovin's Veto@WAR@NM@9 Un.@R$9,99"}}) == 0


def test_card():
    assert get_card("Mana vault") == "Mana Vault"
    assert get_card("asdasdas") is None
    assert get_card("Mana vaul") == "Mana Vault"
