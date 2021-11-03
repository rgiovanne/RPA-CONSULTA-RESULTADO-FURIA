# coding=utf-8
from resource.placarFuria import buscar as buscaPlacar


def buscar():
    print('RODANDO...')

    try:

        return buscaPlacar()

    except Exception as e:

        return (str(e))


if(__name__ == "__main__"):

    for retorno in buscar():
        print(retorno)
