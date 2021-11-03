# coding=utf-8

import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from config.profile import perfil
from selenium.common.exceptions import NoSuchElementException


def buscar():
    print('Configurando navegador')
    url = 'https://www.hltv.org/results?team=8297'
    erro = False
    msgErro = ''
    cont = 0
    codErro = None
    directory = os.path.split(
        os.path.split(os.path.realpath(__file__))[0])[0]
    directory = os.path.join(directory, 'arquivos')
    driver = perfil(False, directory)

    driver.get(url)

    def existeElemento(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    try:
        print("Executando...")
        time.sleep(3)
        element = '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"]'
        while (existeElemento(element) == False and erro == False):
            time.sleep(10)
            if cont > 6:
                msgErro = "site nao carregado; Campo Allow selection não encontrado"
                cont = 0
                erro = True
            else:
                cont = cont + 1
        driver.find_element_by_xpath(element).click()

        element = "//*[@class='results-all']"

        while (existeElemento(element) == False and erro == False):
            time.sleep(10)
            if cont > 6:
                msgErro = "Campo results-all não encontrado"
                cont = 0
                erro = True
            else:
                cont = cont + 1
        element = driver.find_element_by_xpath(element)
        html_content = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = soup.find(name='div')
        resultados = []
        for div in list(divs):
            df_full = pd.read_html(str(div))[0]
            resultado = df_full.to_dict('records')[0]
            resultados.append(
                f"Resultado: {resultado[0]} {resultado[1]} {resultado[2]}\
                                       Campeonato: {resultado[3]}")
        driver.quit()
        return resultados

    except Exception as e:
        driver.quit()
        return str(e)
