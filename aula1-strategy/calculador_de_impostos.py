# -*- coding: UTF-8 -*-
# calculador_de_impostos.py

from impostos import calcula_ISS, calcula_ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, calcule_imposto):
        valor_calculado = calcule_imposto(orcamento)
        print(valor_calculado)


if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(
        orcamento, calcula_ICMS)  # imprimie 50.0
    calculador_de_impostos.realiza_calculo(
        orcamento, calcula_ISS)  # imprime 30.0
