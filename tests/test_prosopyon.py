"""Testes sem webcam e sem face_recognition: so o que nao depende de hardware."""
import os

import prosopyon


def test_cadastro_e_login_usam_a_mesma_pasta():
    # O bug original: gravava em imagens/ e lia de images/.
    pasta_cad = os.path.dirname(prosopyon.caminho_cadastro("ana"))
    pasta_log = os.path.dirname(prosopyon.caminho_login("ana"))
    assert pasta_cad == pasta_log == prosopyon.PASTA_IMAGENS


def test_nomes_dos_arquivos():
    assert prosopyon.caminho_cadastro("ana").endswith("ana.png")
    assert prosopyon.caminho_login("ana").endswith("ana_desconhecido.png")


def test_mensagem_resultado():
    assert prosopyon.mensagem_resultado([True])[0] == "Usuario identificado!"
    assert prosopyon.mensagem_resultado([False])[0].startswith("Usuario nao corresponde")
    assert prosopyon.mensagem_resultado([])[0].startswith("Usuario nao corresponde")
