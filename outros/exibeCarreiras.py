from Model.Carreiras import Carreira
from Repository.CarreirasRepo import listaDeCarreiras


def exibeCarreiras():
    for carreira in listaDeCarreiras:
        Carreira.exibir(carreira)